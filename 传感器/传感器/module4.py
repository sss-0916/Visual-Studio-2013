%卡尔曼滤波和最小二乘法
clear 
%赋初值,系统参数设置 
A = 1; %这个房间的温度是跟前一时刻的温度相同则A=1 
H = 1; %测量系统的参数 
Q = 4; %量测噪声 
R = 1; %系统噪声 
s(1) = 25; %假设房间当前真实温度为25度 
N = 100; %设置 100 个数 
w = randn(1, N); %产生正态分布伪随机信号，即模拟随机产生噪声信号
v = randn(1, N); 
v(1) = 0; 
for k = 2 : N; s(k) = A * s(k - 1) + w(k - 1); %没有控制量u（k）= 0 
z(k) = H * s(k) + v(k-1); 
end 
x(1) = 25; 
for t = 2 : N; 
xpred(t) = A * x(t - 1); 
vpred(t) = A * v(t - 1) * A' + Q; 
k(t) = (vpred(t) * H) / (H * vpred(t) * H' + R); 
x(t) = xpred(t) + k(t) * (z(t) - H * xpred(t)); 
v(t) = (1 - k(t) * H) * vpred(t); 
end 
p = polyfit(x, z, 3); 
f = polyval(p, x); 
t = 1 : N; 
plot(t, x, 'r', t, z, 'g', t, s, 'k', t, f, 'b*-'); 
xlabel('时间/s')
ylabel('温度/℃') 
grid on 
legend('卡尔曼滤波', '观测值', '真实值', '最小二乘滤波') 
title('卡尔曼滤波与最小二乘滤波仿真图') 