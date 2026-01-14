#include <iostream>
#include <fstream>
#include <cmath>
#include <direct.h>
#include <string>
#include <windows.h>

using namespace std;

struct Params {
    double alpha;
    double beta;
    double gamma;
    double delta;

    Params(double a = 0, double b = 0, double g = 0, double d = 0)
        : alpha(a), beta(b), gamma(g), delta(d) {
    }
};

struct State {
    double prey;
    double predator;

    State(double x = 0, double y = 0) : prey(x), predator(y) {}
};

void derivatives(const State& s, const Params& p, State& deriv) {
    deriv.prey = (p.alpha - p.beta * s.predator) * s.prey;
    deriv.predator = (-p.gamma + p.delta * s.prey) * s.predator;
}

State euler(const State& s, const Params& p, double dt) {
    State deriv;
    derivatives(s, p, deriv);
    return State(
        s.prey + deriv.prey * dt,
        s.predator + deriv.predator * dt
    );
}

State rk4(const State& s, const Params& p, double dt) {
    State k1, k2, k3, k4, temp;

    derivatives(s, p, k1);

    temp.prey = s.prey + k1.prey * dt / 2.0;
    temp.predator = s.predator + k1.predator * dt / 2.0;
    derivatives(temp, p, k2);

    temp.prey = s.prey + k2.prey * dt / 2.0;
    temp.predator = s.predator + k2.predator * dt / 2.0;
    derivatives(temp, p, k3);

    temp.prey = s.prey + k3.prey * dt;
    temp.predator = s.predator + k3.predator * dt;
    derivatives(temp, p, k4);

    return State(
        s.prey + (k1.prey + 2 * k2.prey + 2 * k3.prey + k4.prey) * dt / 6.0,
        s.predator + (k1.predator + 2 * k2.predator + 2 * k3.predator + k4.predator) * dt / 6.0
    );
}

bool createDirectory(const string& path) {
    if (_mkdir(path.c_str()) == 0) {
        return true;
    }
    return true;
}

void simulate(const string& data_folder, const string& name,
    const Params& p, const State& init, double T, double dt) {

    ofstream file_prey_euler(data_folder + "\\" + name + "_prey_euler.csv");
    ofstream file_pred_euler(data_folder + "\\" + name + "_pred_euler.csv");
    ofstream file_prey_rk4(data_folder + "\\" + name + "_prey_rk4.csv");
    ofstream file_pred_rk4(data_folder + "\\" + name + "_pred_rk4.csv");
    ofstream file_phase_euler(data_folder + "\\" + name + "_phase_euler.csv");
    ofstream file_phase_rk4(data_folder + "\\" + name + "_phase_rk4.csv");

    file_prey_euler << "Time,Prey\n";
    file_pred_euler << "Time,Predator\n";
    file_prey_rk4 << "Time,Prey\n";
    file_pred_rk4 << "Time,Predator\n";
    file_phase_euler << "Prey,Predator\n";
    file_phase_rk4 << "Prey,Predator\n";

    State s_euler = init;
    State s_rk4 = init;

    double t = 0;
    int steps = static_cast<int>(T / dt);

    for (int i = 0; i <= steps; ++i) {
        file_prey_euler << t << "," << s_euler.prey << "\n";
        file_pred_euler << t << "," << s_euler.predator << "\n";
        file_prey_rk4 << t << "," << s_rk4.prey << "\n";
        file_pred_rk4 << t << "," << s_rk4.predator << "\n";
        file_phase_euler << s_euler.prey << "," << s_euler.predator << "\n";
        file_phase_rk4 << s_rk4.prey << "," << s_rk4.predator << "\n";

        s_euler = euler(s_euler, p, dt);
        s_rk4 = rk4(s_rk4, p, dt);
        t += dt;
    }

    file_prey_euler.close();
    file_pred_euler.close();
    file_prey_rk4.close();
    file_pred_rk4.close();
    file_phase_euler.close();
    file_phase_rk4.close();
}

int main() {
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);
  
    string base_folder = "C:\\Users\\Veronika\\Desktop\\ChM_laba8";
    string data_folder = base_folder + "\\data";
    string graphs_folder = base_folder + "\\graphs";

    createDirectory(base_folder);
    createDirectory(data_folder);
    createDirectory(graphs_folder);

    string system_name = "Совы_Мыши";

    // Параметры из задания
    double alpha = 0.28;     
    double beta = 0.00045;   
    double gamma = 0.42;       
    double delta = 0.00032;   

    double t0 = 0.0;     
    double T = 400.0;    
    double dt = 0.005;     
    double eps = 0.01;   

    double x_star = gamma / delta;     
    double y_star = alpha / beta;       

    double x_eq = x_star;
    double y_eq = y_star;

    double x_pert = x_star * (1.0 + eps);
    double y_pert = y_star * (1.0 - eps);

    Params p(alpha, beta, gamma, delta);
    State init_pert(x_pert, y_pert);

    string name_pert = system_name + "_pert";
    simulate(data_folder, name_pert, p, init_pert, T, dt);

    State init_eq(x_eq, y_eq);
    string name_eq = system_name + "_eq";
    simulate(data_folder, name_eq, p, init_eq, T, dt);

    State init_original(600, 1000);
    string name_original = system_name + "_original_x0_lt_y0";
    simulate(data_folder, name_original, p, init_original, T, dt);

    return 0;
}
