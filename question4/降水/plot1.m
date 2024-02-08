% 生成X轴和Y轴的数据点
x = linspace(20, 160, 30); % 降水量，范围是20-160mm，分为100份
y = linspace(74.2, 74.8, 30); % 水位，范围是74.2-74.8mm，也分为100份

% 使用meshgrid生成网格点坐标
[X, Y] = meshgrid(x, y);

% 假设correlationMatrix是您的相关系数矩阵，这里我们使用随机数据来模拟
% 实际应用中，您应该使用实际计算出的相关系数矩阵替换这里的随机矩阵
% Z = rand(100, 100); % 模拟相关系数矩阵，实际中请用实际数据替代
Z=correlationMatrix;

% 绘制三维图
% surf(X, Y, Z) % 使用surf函数绘制三维表面图
surf(X,Y,reshape(Z,30));
colorbar % 显示颜色条，颜色条表示Z轴的值的大小
xlabel('Precipitation (mm)') % X轴标签
ylabel('Water Level (mm)') % Y轴标签
zlabel('Correlation Coefficient') % Z轴标签
title('3D Plot of Correlation Coefficient between Precipitation and Water Level') % 图标题