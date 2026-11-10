import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    """Строит график зависимости напряжения от времени и сохраняет его в файл."""
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.xlim(time[0], time[-1] if len(time) > 1 else time[0] + 1)
    plt.ylim(0, max_voltage)
    plt.grid(True)

    # СОХРАНЕНИЕ ГРАФИКА В ФАЙЛ
    filename = "RC1_voltage_plot.png"
    plt.savefig(filename, dpi=300)
    print(f"График напряжения сохранен в файл {filename}")
    plt.show()
    plt.close()


def plot_sampling_period_hist(time):
    """Строит распределение количества измерений по их продолжительности и сохраняет в файл."""
    sampling_periods = []
    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i - 1])

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.title("Распределение периодов измерений")
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.06)
    plt.grid(True)

    # СОХРАНЕНИЕ ГИСТОГРАММЫ В ФАЙЛ
    filename = "RC1_histogram_plot.png"
    plt.savefig(filename, dpi=300)
    print(f"Гистограмма сохранена в файл {filename}")
    plt.show()
    plt.close()


# ПРИМЕР ВЫЗОВА (замените на свои реальные списки time и voltage):
# time_data = [0, 0.1, 0.2, 0.3, 0.4]
# voltage_data = [0, 1.2, 2.5, 3.1, 3.8]
# plot_voltage_vs_time(time_data, voltage_data, max_voltage=5.0)
# plot_sampling_period_hist(time_data)
