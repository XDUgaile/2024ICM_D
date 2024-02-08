% 假设 waterLevels 和 precipitations 已经在工作空间中定义

% 步骤 1: 计算每个变量的累积分布函数值
u = unifcdf(waterLevels, min(waterLevels(:)), max(waterLevels(:)));
v = unifcdf(precipitations, min(precipitations(:)), max(precipitations(:)));

% 步骤 2: 使用Frank Copula
% 选择一个合适的theta值，theta值控制Copula的相关性
theta = 1; % 这个值可以通过拟合数据来选择
% 计算Frank Copula的联合CDF值
jointCdf = copulacdf('Frank', [u(:), v(:)], theta);

% 步骤 3: 绘制联合CDF的散点图
scatter(u(:), v(:), [], jointCdf, 'filled');
colorbar; % 显示颜色条以表示联合CDF的值
title('Frank Copula的联合CDF');
xlabel('水位数据的CDF');
ylabel('降水数据的CDF');