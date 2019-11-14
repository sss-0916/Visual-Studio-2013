%Kalman

x = 0 : 0.01 * pi : 2 * pi;
y = sin(x);
Vw = 0.1;
w = normrnd(0, Vw, 1, length(x));
z = y + w;
Vw1 = w * w' / length(x);
P(1) = Vw; S(1) = y(1); Vw1 = Vw; Vu(1) = 0;
for n = 2 : length(x);
    P_(n) = P(n - 1) + 0;
    K(n) = P_(n) / (P_(n) + Vw1(n-1));
    S(n) = S(n-1) + K(n) * (z(n) - S(n-1));
    P(n) = (1 - K(n)) * P_(n);
    u(n) = S(n) - S(n-1);
    W(n) = z(n) - S(n);                                          
    Vw1(n) = W(1 : n) * W(1 : n)' / n;
    Vu(n) = u(1 : n) * u(1 : n)' / n;
end
plot(x, y, '-', x, z, 'o', x, S, '.-');
grid on
legend('truth', 'observation', 'kalmen estimate');