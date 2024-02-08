function plotPrecipitationWaterLevel()
    N = 10000; % 数据点数量
    
    % 生成模拟的降水量数据，范围从20到170mm
    precipitation = 20 + (170-20) * rand(N, 1);
    
    % 生成模拟的水位数据，范围从74到76m
    waterLevel = 74 + (76-74) * rand(N, 1);
    
    % 绘制散点图
    scatter(precipitation, waterLevel, 'filled');
    title('Water Level vs. Precipitation');
    xlabel('Precipitation (mm)');
    ylabel('Water Level (m)');
    
    % 调整坐标轴范围以更好地展示数据
    xlim([20, 170]);
    ylim([74, 76]);
end