#include <verilated.h>
#include "Vtb_fir.h"
#include <iostream>

int main(int argc, char** argv) {
    VerilatedContext* contextp = new VerilatedContext;
    contextp->commandArgs(argc, argv);
    
    Vtb_fir* top = new Vtb_fir{contextp};

    std::cout << "--- Начало симуляции ---" << std::endl;
    
    // Главный цикл симуляции
    while (!contextp->gotFinish()) {
        top->eval();             // Выполнить логику
        contextp->timeInc(1);    // Продвинуть время на 1 шаг (1 нс)
    }
    
    std::cout << "--- Конец симуляции ---" << std::endl;

    top->final();
    delete top;
    delete contextp;
    return 0;
}