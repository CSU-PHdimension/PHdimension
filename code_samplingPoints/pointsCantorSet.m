function  points = pointsCantorSet(numpoints,level)
% Samples points from the "Cantor set". More precisely, samples points from
% the left endpoints (equivalently the midpoints, after a translation) of
% the intervals in the Cantor set at a specified level.

points=zeros(numpoints,1);
binarySequences=randi(2,numpoints,level)-1;
for i=1:level
    points=points+2*binarySequences(:,i)/(3^i);
end

%scatter(points,zeros(numpoints,1),'.')