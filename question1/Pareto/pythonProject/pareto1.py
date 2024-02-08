import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 将给定的解存储在DataFrame中
data = pd.DataFrame({


'Objective 1': [ 0.097, 0.043, 0.079, 0.012, 0.033, 0.037, 0.046, 0.085, 0.058, 0.089, 0.09, 0.042, 0.055, 0.083, 0.003, 0.041, 0.047, 0.007, 0.02, 0.08, 0.026, 0.076, 0.059, 0.049, 0.058, 0.095, 0.035, 0.028, 0.012, 0.093, 0.012, 0.095, 0.04, 0.024, 0.06, 0.046, 0.01, 0.089, 0.047, 0.055, 0.052, 0.089, 0.058, 0.023, 0.012, 0.031, 0.022, 0.025, 0.005, 0.093, 0.039, 0.073, 0.057, 0.094, 0.055, 0.041, 0.052, 0.099, 0.017, 0.07, 0.005, 0.019, 0.025, 0.05, 0.08, 0.088, 0.052, 0.05, 0.016, 0.092, 0.072, 0.058, 0.1, 0.089, 0.019, 0.028, 0.049, 0.018, 0.088, 0.052, 0.074, 0.086, 0.065, 0.051, 0.068, 0.056, 0.08, 0.054, 0.018, 0.085, 0.049, 0.059, 0.006, 0.044, 0.063, 0.053, 0.042, 0.094, 0.026, 0.055, 0.05, 0.038, 0.079, 0.058, 0.044, 0.073, 0.098, 0.082, 0.045, 0.003, 0.058, 0.03, 0.042, 0.076, 0.064, 0.059, 0.045, 0.087, 0.049, 0.083, 0.055, 0.013, 0.098, 0.069, 0.076, 0.055, 0.011, 0.044, 0.07, 0.084, 0.099, 0.051, 0.048, 0.012, 0.059, 0.009, 0.007, 0.08, 0.055, 0.092, 0.05, 0.056, 0.045, 0.057, 0.015, 0.034, 0.068, 0.071, 0.097, 0.008, 0.059, 0.045, 0.068, 0.082, 0.059, 0.043, 0.048, 0.083, 0.078, 0.006, 0.038, 0.081, 0.095, 0.073, 0.031, 0.021, 0.062, 0.08, 0.031, 0.037, 0.065, 0.075, 0.088, 0.011, 0.077, 0.025, 0.023, 0.084, 0.045, 0.099, 0.014, 0.006, 0.047, 0.012, 0.06, 0.079, 0.009, 0.087, 0.079, 0.039, 0.039, 0.09, 0.052, 0.058, 0.023, 0.026, 0.04, 0.086, 0.08, 0.072, 0.063, 0.027, 0.03, 0.096, 0.082, 0.051, 0.039, 0.095, 0.062, 0.082, 0.07, 0.05, 0.077, 0.052, 0.071, 0.056, 0.063, 0.007, 0.088, 0.069, 0.026, 0.064, 0.0, 0.094, 0.064, 0.088, 0.073, 0.047, 0.059, 0.03, 0.062, 0.08, 0.094, 0.03, 0.077, 0.058, 0.05, 0.041, 0.015, 0.037, 0.002, 0.009, 0.054, 0.051, 0.0, 0.012, 0.063, 0.082, 0.014, 0.061, 0.084, 0.049, 0.041, 0.029, 0.012, 0.044, 0.06, 0.096, 0.01, 0.065, 0.057, 0.013, 0.088, 0.024, 0.011, 0.1, 0.048, 0.054, 0.067, 0.076, 0.041, 0.019, 0.054, 0.036, 0.048, 0.033, 0.008, 0.016, 0.028, 0.079, 0.089, 0.052, 0.093, 0.033, 0.092, 0.014, 0.033, 0.097, 0.054, 0.099, 0.027, 0.084, 0.017, 0.061, 0.031, 0.057, 0.008, 0.005, 0.038, 0.036, 0.086, 0.033, 0.056, 0.076, 0.086, 0.022, 0.045, 0.042, 0.076, 0.089, 0.038, 0.044, 0.016, 0.071, 0.062, 0.085, 0.045, 0.057, 0.013, 0.079, 0.012, 0.06, 0.018, 0.026, 0.044, 0.034, 0.002, 0.096, 0.084, 0.097, 0.054, 0.025, 0.034, 0.022, 0.07, 0.081, 0.012, 0.076, 0.067, 0.062, 0.042, 0.013, 0.004, 0.024, 0.013, 0.018, 0.068, 0.039, 0.089, 0.038, 0.047, 0.02, 0.001, 0.067, 0.023, 0.061, 0.092, 0.03, 0.056, 0.022, 0.038, 0.011, 0.019, 0.008, 0.01, 0.021, 0.01, 0.016, 0.085, 0.076, 0.052, 0.064, 0.02, 0.053, 0.007, 0.013, 0.026, 0.015, 0.082, 0.1, 0.003, 0.058, 0.021, 0.014, 0.054, 0.038, 0.001, 0.07, 0.003, 0.02, 0.011, 0.058, 0.021, 0.071, 0.034, 0.024, 0.093, 0.085, 0.082, 0.045, 0.012, 0.072, 0.03, 0.093, 0.088, 0.033, 0.053, 0.049, 0.04, 0.088, 0.05, 0.086, 0.066, 0.083, 0.006, 0.068, 0.053, 0.082, 0.07, 0.038, 0.062, 0.001, 0.026, 0.03, 0.061, 0.073, 0.095, 0.002, 0.076, 0.035, 0.014, 0.091, 0.019, 0.039, 0.1, 0.019, 0.088, 0.077, 0.088, 0.052, 0.099, 0.098, 0.075, 0.083, 0.035, 0.057, 0.093, 0.079, 0.061, 0.008, 0.01, 0.032, 0.047, 0.035, 0.016, 0.08, 0.08, 0.049, 0.061, 0.056, 0.098, 0.052, 0.098, 0.072, 0.03, 0.045, 0.012, 0.052, 0.016, 0.058, 0.016, 0.054, 0.014, 0.043, 0.099, 0.033, 0.089, 0.066, 0.07, 0.092, 0.066, 0.014, 0.059, 0.086, 0.086, 0.06, 0.003, 0.07, 0.045, 0.054, 0.042, 0.024, 0.082, 0.018, 0.025, 0.02, 0.009, 0.092, 0.074, 0.034],

'Objective 2': [ 0.1, 0.048, 0.081, 0.016, 0.038, 0.038, 0.05, 0.088, 0.059, 0.096, 0.093, 0.045, 0.055, 0.092, 0.009, 0.049, 0.054, 0.015, 0.029, 0.087, 0.031, 0.085, 0.059, 0.052, 0.061, 0.1, 0.042, 0.034, 0.012, 0.094, 0.015, 0.098, 0.048, 0.031, 0.063, 0.054, 0.014, 0.092, 0.053, 0.061, 0.054, 0.091, 0.062, 0.023, 0.021, 0.033, 0.029, 0.026, 0.009, 0.097, 0.049, 0.078, 0.06, 0.1, 0.061, 0.049, 0.054, 0.1, 0.018, 0.072, 0.013, 0.022, 0.029, 0.054, 0.082, 0.088, 0.055, 0.053, 0.021, 0.094, 0.082, 0.064, 0.1, 0.092, 0.026, 0.03, 0.057, 0.024, 0.089, 0.059, 0.08, 0.096, 0.065, 0.056, 0.071, 0.058, 0.085, 0.063, 0.024, 0.093, 0.053, 0.063, 0.01, 0.052, 0.068, 0.059, 0.048, 0.096, 0.03, 0.06, 0.059, 0.04, 0.08, 0.063, 0.05, 0.078, 0.099, 0.087, 0.055, 0.004, 0.068, 0.036, 0.045, 0.079, 0.068, 0.065, 0.05, 0.088, 0.055, 0.089, 0.061, 0.014, 0.1, 0.074, 0.077, 0.063, 0.011, 0.046, 0.075, 0.094, 0.099, 0.059, 0.051, 0.021, 0.067, 0.015, 0.008, 0.088, 0.058, 0.095, 0.051, 0.056, 0.054, 0.062, 0.019, 0.034, 0.069, 0.077, 0.1, 0.009, 0.066, 0.054, 0.077, 0.089, 0.061, 0.047, 0.054, 0.09, 0.079, 0.007, 0.043, 0.089, 0.1, 0.075, 0.035, 0.024, 0.067, 0.088, 0.035, 0.041, 0.067, 0.077, 0.091, 0.012, 0.087, 0.025, 0.03, 0.085, 0.054, 0.1, 0.024, 0.014, 0.055, 0.019, 0.068, 0.088, 0.011, 0.096, 0.083, 0.046, 0.048, 0.099, 0.057, 0.059, 0.028, 0.028, 0.045, 0.086, 0.088, 0.078, 0.069, 0.033, 0.031, 0.098, 0.091, 0.052, 0.042, 0.1, 0.071, 0.087, 0.071, 0.058, 0.087, 0.06, 0.08, 0.063, 0.065, 0.013, 0.096, 0.078, 0.033, 0.066, 0.008, 0.1, 0.073, 0.097, 0.076, 0.05, 0.061, 0.038, 0.07, 0.084, 0.1, 0.039, 0.083, 0.062, 0.053, 0.043, 0.018, 0.037, 0.011, 0.011, 0.056, 0.053, 0.001, 0.02, 0.068, 0.082, 0.018, 0.067, 0.09, 0.059, 0.05, 0.034, 0.017, 0.045, 0.066, 0.098, 0.014, 0.073, 0.058, 0.021, 0.097, 0.028, 0.018, 0.1, 0.054, 0.056, 0.075, 0.083, 0.046, 0.021, 0.059, 0.044, 0.052, 0.039, 0.011, 0.02, 0.03, 0.086, 0.093, 0.052, 0.1, 0.034, 0.098, 0.022, 0.038, 0.1, 0.059, 0.1, 0.031, 0.085, 0.024, 0.068, 0.034, 0.064, 0.008, 0.008, 0.041, 0.042, 0.09, 0.04, 0.061, 0.084, 0.088, 0.027, 0.048, 0.046, 0.084, 0.099, 0.044, 0.052, 0.017, 0.071, 0.067, 0.086, 0.045, 0.062, 0.022, 0.081, 0.017, 0.069, 0.027, 0.032, 0.051, 0.037, 0.007, 0.098, 0.089, 0.1, 0.055, 0.029, 0.043, 0.024, 0.07, 0.088, 0.019, 0.078, 0.073, 0.071, 0.046, 0.014, 0.013, 0.029, 0.022, 0.026, 0.077, 0.041, 0.098, 0.045, 0.049, 0.023, 0.009, 0.068, 0.027, 0.07, 0.098, 0.032, 0.061, 0.032, 0.039, 0.011, 0.027, 0.016, 0.015, 0.029, 0.015, 0.024, 0.093, 0.077, 0.057, 0.067, 0.03, 0.055, 0.014, 0.017, 0.034, 0.019, 0.091, 0.1, 0.005, 0.065, 0.027, 0.024, 0.057, 0.042, 0.008, 0.078, 0.005, 0.028, 0.014, 0.058, 0.021, 0.075, 0.036, 0.025, 0.094, 0.092, 0.088, 0.052, 0.017, 0.072, 0.038, 0.094, 0.097, 0.035, 0.054, 0.055, 0.043, 0.09, 0.06, 0.094, 0.072, 0.086, 0.014, 0.073, 0.061, 0.089, 0.075, 0.04, 0.066, 0.009, 0.03, 0.037, 0.065, 0.073, 0.099, 0.007, 0.078, 0.038, 0.016, 0.1, 0.021, 0.041, 0.1, 0.023, 0.091, 0.083, 0.094, 0.053, 0.1, 0.1, 0.079, 0.084, 0.042, 0.062, 0.096, 0.084, 0.068, 0.012, 0.012, 0.037, 0.05, 0.044, 0.024, 0.085, 0.088, 0.051, 0.065, 0.063, 0.099, 0.058, 0.1, 0.077, 0.033, 0.05, 0.013, 0.059, 0.026, 0.063, 0.026, 0.064, 0.022, 0.047, 0.1, 0.037, 0.095, 0.076, 0.071, 0.099, 0.067, 0.018, 0.066, 0.088, 0.094, 0.061, 0.01, 0.078, 0.053, 0.064, 0.049, 0.028, 0.083, 0.021, 0.03, 0.02, 0.013, 0.099, 0.077, 0.039],

'Objective 3': [ 0.1, 0.054, 0.09, 0.018, 0.046, 0.038, 0.053, 0.093, 0.067, 0.1, 0.096, 0.046, 0.061, 0.096, 0.015, 0.052, 0.059, 0.016, 0.032, 0.088, 0.036, 0.093, 0.062, 0.058, 0.07, 0.1, 0.044, 0.044, 0.021, 0.1, 0.018, 0.1, 0.054, 0.036, 0.063, 0.054, 0.016, 0.1, 0.059, 0.065, 0.062, 0.099, 0.064, 0.024, 0.031, 0.039, 0.036, 0.027, 0.018, 0.097, 0.054, 0.085, 0.061, 0.1, 0.07, 0.052, 0.063, 0.1, 0.019, 0.076, 0.02, 0.031, 0.031, 0.058, 0.085, 0.097, 0.063, 0.062, 0.026, 0.096, 0.088, 0.067, 0.1, 0.099, 0.027, 0.03, 0.063, 0.029, 0.089, 0.061, 0.088, 0.098, 0.068, 0.065, 0.08, 0.067, 0.095, 0.072, 0.025, 0.094, 0.056, 0.066, 0.011, 0.057, 0.073, 0.064, 0.057, 0.098, 0.039, 0.07, 0.062, 0.048, 0.084, 0.068, 0.056, 0.087, 0.1, 0.095, 0.06, 0.013, 0.078, 0.045, 0.049, 0.087, 0.07, 0.073, 0.06, 0.097, 0.061, 0.094, 0.068, 0.018, 0.1, 0.076, 0.078, 0.07, 0.012, 0.05, 0.078, 0.1, 0.1, 0.065, 0.057, 0.029, 0.074, 0.025, 0.016, 0.093, 0.065, 0.1, 0.06, 0.061, 0.064, 0.063, 0.023, 0.036, 0.071, 0.084, 0.1, 0.015, 0.073, 0.056, 0.083, 0.098, 0.061, 0.056, 0.063, 0.098, 0.083, 0.01, 0.052, 0.098, 0.1, 0.085, 0.037, 0.029, 0.069, 0.095, 0.04, 0.043, 0.072, 0.081, 0.098, 0.02, 0.094, 0.032, 0.032, 0.09, 0.063, 0.1, 0.031, 0.02, 0.059, 0.025, 0.07, 0.095, 0.013, 0.1, 0.083, 0.055, 0.049, 0.1, 0.064, 0.06, 0.03, 0.036, 0.05, 0.094, 0.092, 0.082, 0.075, 0.04, 0.041, 0.1, 0.1, 0.053, 0.043, 0.1, 0.081, 0.093, 0.073, 0.061, 0.094, 0.068, 0.083, 0.073, 0.066, 0.016, 0.1, 0.081, 0.034, 0.068, 0.016, 0.1, 0.077, 0.098, 0.081, 0.054, 0.069, 0.039, 0.078, 0.084, 0.1, 0.043, 0.093, 0.071, 0.063, 0.045, 0.02, 0.037, 0.016, 0.011, 0.062, 0.062, 0.008, 0.027, 0.069, 0.086, 0.025, 0.076, 0.094, 0.06, 0.05, 0.038, 0.021, 0.047, 0.074, 0.099, 0.021, 0.078, 0.066, 0.029, 0.099, 0.032, 0.019, 0.1, 0.058, 0.058, 0.08, 0.091, 0.055, 0.025, 0.066, 0.046, 0.055, 0.047, 0.019, 0.022, 0.037, 0.09, 0.093, 0.055, 0.1, 0.035, 0.098, 0.023, 0.041, 0.1, 0.065, 0.1, 0.036, 0.086, 0.033, 0.076, 0.037, 0.069, 0.008, 0.014, 0.044, 0.042, 0.092, 0.047, 0.062, 0.092, 0.094, 0.036, 0.049, 0.052, 0.089, 0.1, 0.049, 0.056, 0.021, 0.078, 0.068, 0.094, 0.047, 0.069, 0.022, 0.09, 0.023, 0.073, 0.027, 0.033, 0.054, 0.047, 0.012, 0.1, 0.092, 0.1, 0.058, 0.031, 0.046, 0.032, 0.077, 0.088, 0.019, 0.087, 0.083, 0.076, 0.05, 0.017, 0.018, 0.035, 0.025, 0.028, 0.081, 0.047, 0.1, 0.048, 0.054, 0.027, 0.015, 0.075, 0.029, 0.072, 0.1, 0.038, 0.07, 0.04, 0.043, 0.015, 0.034, 0.023, 0.022, 0.036, 0.019, 0.03, 0.097, 0.084, 0.058, 0.07, 0.032, 0.062, 0.015, 0.024, 0.04, 0.024, 0.1, 0.1, 0.013, 0.074, 0.029, 0.034, 0.061, 0.044, 0.013, 0.079, 0.007, 0.031, 0.023, 0.066, 0.03, 0.085, 0.041, 0.029, 0.097, 0.1, 0.092, 0.057, 0.02, 0.077, 0.043, 0.095, 0.1, 0.039, 0.055, 0.061, 0.045, 0.094, 0.069, 0.097, 0.077, 0.094, 0.023, 0.073, 0.07, 0.098, 0.079, 0.049, 0.074, 0.012, 0.035, 0.039, 0.067, 0.078, 0.1, 0.014, 0.088, 0.043, 0.018, 0.1, 0.026, 0.048, 0.1, 0.03, 0.097, 0.088, 0.1, 0.061, 0.1, 0.1, 0.083, 0.091, 0.044, 0.066, 0.1, 0.088, 0.078, 0.013, 0.015, 0.044, 0.054, 0.044, 0.031, 0.086, 0.091, 0.058, 0.072, 0.067, 0.1, 0.064, 0.1, 0.08, 0.036, 0.053, 0.022, 0.059, 0.028, 0.071, 0.034, 0.07, 0.029, 0.054, 0.1, 0.038, 0.1, 0.084, 0.081, 0.1, 0.075, 0.021, 0.073, 0.09, 0.099, 0.062, 0.019, 0.087, 0.06, 0.068, 0.052, 0.037, 0.089, 0.021, 0.033, 0.026, 0.017, 0.099, 0.077, 0.045]




})

# 使用Matplotlib创建三维散点图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制数据点
ax.scatter(data['Objective 1'], data['Objective 2'], data['Objective 3'], c='blue', marker='o')

ax.set_xlabel('Objective 1')
ax.set_ylabel('Objective 2')
ax.set_zlabel('Objective 3')
ax.set_title('3D Scatter Plot of Solutions on Pareto Front')

plt.show()