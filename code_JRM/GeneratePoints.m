%% Script for generating sequences of point clouds.
% (It might be better in the future to save distance matrices instead of 
% point cloud data.)

%% Settings
start = 50;
inc = 50;
final = 10000;
level = 100000; % For cantor set constructions. We've usually used 10^6.
dir='CantorSetCrossInterval/'; % Construct directory exists before running!

%% Create point cloud data
% Change the function called in the loop to sample different spaces.
for i = start:inc:final
%     points = pointsCantorSet(i,level);
    points = pointsCantorSetCrossInterval(i,level);
%     points = pointsCantorDust2D(i,level);
%     points = pointsCantorDust3D(i,level);
    csvwrite([dir,'points_',int2str(i),'.csv'],points);
end