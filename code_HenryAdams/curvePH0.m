function edgeLengths = curvePH0(numpoints)

% This code computes the edge lengths of a minimal spanning tree, and plots the sorted edge lengths as a step function.

% These step functions could be plotted so that the largest y-value is the
% length of the longest edge. However, that doesn't allow us to
% experimentally estimate the fractal dimension d. We instead choose the
% y-axis scaling as a constant times numpoints^(1/d)

addpath kruskal
disp('Sampling points...')

% point_cloud = rand(numpoints,1);
% verticalAxisScale = 6/numpoints;
% name = 'Interval-0';

% point_cloud = rand(numpoints,2); % points on square
% verticalAxisScale = 1.8/numpoints^(1/2);
% name = 'Square-0';

% point_cloud = pointsDiskAreaOne(numpoints);
% verticalAxisScale = 1.8/numpoints^(1/2);
% name = 'Disk-0';

% point_cloud = pointsTriangleAreaOne(numpoints);
% verticalAxisScale = 1.8/numpoints^(1/2);
% name = 'Triangle-0';

% point_cloud = rand(numpoints,3);
% verticalAxisScale = 1.7/numpoints^(1/3);
% name = 'Cube-0';

% level = 100000;
% point_cloud = pointsCantorSet(numpoints,level);
% verticalAxisScale = 1000/numpoints^(log(3)/log(2));
% name = 'Cantor-0';

% level = 100000;
% point_cloud = pointsCantorSet(numpoints,level);
% verticalAxisScale = 1000/numpoints^(log(3)/log(2));
% name = 'Cantor-0';
 
 level = 100000;
 point_cloud = pointsCantorSetCrossInterval(numpoints,level);
 verticalAxisScale = 5/numpoints^(1/(1+log(2)/log(3)));
 name = 'CantorCrossInterval-0-dim1plus';
% verticalAxisScale = 5/numpoints^(1/2);
% name = 'CantorCrossInterval-0-dim2';

% level = 100000;
% point_cloud = pointsCantorDust2D(numpoints,level);
% verticalAxisScale = 30/numpoints^(log(3)/log(4));
% name = 'CantorDust2D-0';

% level = 100000;
% point_cloud = pointsCantorDust3D(numpoints,level);
% verticalAxisScale = 8/numpoints^(log(3)/log(8));
% name = 'CantorDust3D-0';

% level = 100000;
% point_cloud = pointsSierpinski2D(numpoints,level);
% verticalAxisScale = 3/numpoints^(log(2)/log(3));
% name = 'Sierpinski2D-0';

disp('Computing the minimal spanning tree...')
% D=squareform(pdist(point_cloud,'euclidean'));
% The above line doesn't work on Henry's office desktop since pdist isn't in Matlab 2012a. Hence we do it manually below
D=zeros(numpoints,numpoints);
for i=1:numpoints
    for j=i+1:numpoints
        dist=norm(point_cloud(i,:)-point_cloud(j,:));
        D(i,j)=dist;
        D(j,i)=dist;
    end
end
[w_st, ST, X_st] = kruskal(ones(numpoints,numpoints)-eye(numpoints), D);
edgeLengths=zeros(1,length(ST));
for i=1:length(ST)
    edgeLengths(i)=D(ST(i,1),ST(i,2));
end
plotStepFunction(sort(edgeLengths),verticalAxisScale);
title([name,'-',int2str(numpoints)])
saveas(gcf,[name,'-',int2str(numpoints)],'png')
% saveas(gcf,['plotsStepFunctions/',name,'-',int2str(numpoints)],'png')
