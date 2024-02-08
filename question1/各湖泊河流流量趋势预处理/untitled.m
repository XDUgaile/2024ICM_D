% 准备数据
months = 1:12; % 代表一月到十二月
SUP = [183.54, 183.36, 183.39, 183.49, 183.53, 183.73, 183.74, 183.76, 183.78, 183.75, 183.87, 183.69];
MIC = [176.39, 176.55, 176.45, 176.71, 176.74, 176.97, 176.95, 177.09, 177.01, 176.95, 176.85, 176.82];
STC = [175.22, 175.16, 175.39, 175.43, 175.57, 175.73, 175.68, 175.63, 175.61, 175.43, 175.47, 175.45];
ERI = [174.21, 174.36, 174.53, 174.69, 174.81, 174.76, 174.74, 174.80, 174.54, 174.57, 174.45, 174.48];
ONT = [74.62, 74.89, 74.90, 75.03, 75.23, 75.26, 75.34, 75.21, 74.85, 74.77, 74.86, 74.75];

% 绘制SUP湖的数据
subplot(3,1,1); % 创建上部的绘图区域
plot(months, SUP, '-o');
legend('SUP');
ylim([183 184]); % 设置纵轴坐标范围
ylabel('Water Level (m)');
title('Water Level of Lake SUP');

% 绘制MIC, STC, ERI湖的数据
subplot(3,1,2); % 创建中部的绘图区域
plot(months, MIC, '-+', months, STC, '-*', months, ERI, '-x');
legend('MIC', 'STC', 'ERI');
ylim([174 178]); % 设置纵轴坐标范围
ylabel('Water Level (m)');
title('Water Levels of Lakes MIC, STC, and ERI');

% 绘制ONT湖的数据
subplot(3,1,3); % 创建底部的绘图区域
plot(months, ONT, '-s');
legend('ONT');
ylim([74 76]); % 设置纵轴坐标范围
ylabel('Water Level (m)');
xlabel('Month');
title('Water Level of Lake ONT');

% 调整subplot的位置和大小，如果需要的话
% 这部分代码略去，因为其需要根据实际显示效果进行调整