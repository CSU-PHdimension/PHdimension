% Script for computing edge lengths from persistence intervals

%% Settings. Edit these for different experiments.
dir='CantorDust3D_katrina/';   % Directory containing ripser output (include trailing 
                    % / ).
fname='Homology_';      % File naming convention.
ftype='.txt';           % File type
name='Cantor Dust in R^3';       % Name of sampled object (for figure titles)
min=50;         % Minimum number of points sampled
inc=50;         % Increment size in sampling
max=3400;       % Maximum number of points sampled
dimn = 0;       % Dimension of homology to look at.

%% Computations.
% Loop through all the files and compute the sum of the edge lengths:
points=min:inc:max;
edges=zeros(size(points));
for i=1:length(points)
    phintervals = ripserToArray([dir,fname,int2str(points(i)),ftype],dimn);
    edges(i) = sum(phintervals(:,2) - phintervals(:,1));
end

%% Make plots.
% Standard linear fit to log-log plot
logedges = log10(edges);
logpoints = log10(points);
p = polyfit(logpoints,logedges,1);
x_max=4.2; x_min=1;
polyx=x_min:.01:x_max;
polyy=p(1)*polyx + p(2);
% Fancy fitting routine
[alpha,c] = extrapolate_asymptotics(points,edges);
asyy = log10(c) + alpha*polyx;
% Make plot of points and both fits
figure;
hold on;
plot(logpoints,logedges,'o');
plot(polyx,polyy);
plot(polyx,asyy);
axis equal;
grid on;
title(['PH_',int2str(dimn),' for points from ',name]);
xlabel('log_{10}(N)');
ylabel(['log_{10}(L^',int2str(dimn),'(X_n))']);
legend(strcat('linear fit= ',num2str(p(1))),'data',strcat('asymptotic estimate=',num2str(alpha)));
