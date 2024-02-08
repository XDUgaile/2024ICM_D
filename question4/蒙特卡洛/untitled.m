function GaussDistributionPlot()
    % 输入期望和方差
    E = input('输入期望:');
    D = input('输入方差:');
    N = 1000; % 生成随机数的数量

    randomNumbers = zeros(N, 1); % 初始化数组以存储随机数

    for j = 1:N
        uni = rand(1, 2); % 生成2个[0,1)区间内的均匀分布随机数
        
        A = sqrt(-2 * log(uni(1)));
        B = 2 * pi * uni(2);
        C = A * cos(B);
        r = E + C * sqrt(D); % 调整以符合给定的期望E和方差D
        
        randomNumbers(j) = r; % 保存随机数
    end

    % 绘制散点图
    scatter(1:N, randomNumbers, 'filled');
    title('Generated Random Numbers');
    xlabel('Sample Index');
    ylabel('Random Number Value');
end