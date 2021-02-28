clc
n = input('Enter size of your A matrix:');

%% construct A''
A_dd = zeros(n,n);

%diagonal case
for i = 1:n
    A_dd(i,i) = -6;
end

%two end points on main diagonal
A_dd(1,2) = 1;
A_dd(n,n-1) = 1;

%for 2nd row to n-1th row
for i = 2:n-1
    A_dd(i,i-1) = 1;
    A_dd(i,i+1) = 1;
end
I = eye(n); %identity of size n*n

%% Construct A'
A_dash = zeros(n^2,n^2);

count = 0;
for i = 1:n
    A_dash((i-1)*n+1:i*n,(i-1)*n+1:i*n) = A_dd;
    
    count = count + 1; 
    %place the I matrix on up and down diagonal
    %there will always be n-1 I matrix on up and down diagnoals
    if count <= n-1
        A_dash((i-1)*n+1:i*n,i*n+1:(i+1)*n) = I;
        A_dash(i*n+1:(i+1)*n,(i-1)*n+1:i*n) = I;
    end
end

%% Construct A
m = n^2;
A = zeros(m^2,m^2);
I = eye(m);

count = 0;
for i = 1:m
    A((i-1)*m+1:i*m,(i-1)*m+1:i*m) = A_dash;
    
    count = count + 1; 
    %place the I matrix on up and down diagonal
    if count <= m-1
        A((i-1)*m+1:i*m,i*m+1:(i+1)*m) = I;
        A(i*m+1:(i+1)*m,(i-1)*m+1:i*m) = I;
    end
end

A