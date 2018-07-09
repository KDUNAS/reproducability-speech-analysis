% problem parameters
h = .1;
m = 1;
M=4;
alpha=0.1;
K = 100;
% way-points
k1=10; w1=[ 2; 2];
k2=30; w2=[ -2; 3];
k3=40; w3=[ 4; -3];
k4=80; w4=[-4; -2];
A = [eye(2) h*eye(2); zeros(2) (1-alpha)*eye(2)];
B = [zeros(2); h/m*eye(2)];
C = [eye(2) zeros(2)];
[n, nn] = size(B);
k = [k1 k2 k3 k4];
G = [];
for i = 1:M
ABmatrix = [];
temp = B;
for j=1:k(i)-1
ABmatrix = [temp ABmatrix];
temp = A*temp;
end
Gi = C*[ABmatrix zeros(n, nn*(K-k(i)+1))];
G = [G; Gi];
end
w = [w1; w2; w3; w4];
u = pinv(G)*w;
% plotting the input
f = [u(1:2:end)'; u(2:2:end)'];
figure;
subplot(211); plot(f(1,:));
subplot(212); plot(f(2,:));
% simulating the system
p = zeros(2,K+1);
v = zeros(2,K+1);
for i=1:K
p(:,i+1) = p(:,i) + h*v(:,i);
v(:,i+1) = (1-alpha)*v(:,i) + h*f(:,i)/m;
end
% Optimal value of J
J = norm(u)^2
figure;
plot(p(1,:),p(2,:));
hold on
ps = [w1 w2 w3 w4];
plot(ps(1,:),ps(2,:),'*');