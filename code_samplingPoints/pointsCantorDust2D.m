function  points = pointsCantorDust2D(numpoints,level)
% Samples points from the "2D Cantor Dust set", which is the Cartesian 
% product of two copies of the Cantor set. More precisely, samples points 
% from the left endpoints (equivalently the midpoints, after a translation)
% of the intervals in the Cantor set at a specified level, and then takes
% the ordered pair of two such random points.

points=zeros(numpoints,2);
points(:,1)=pointsCantorSet(numpoints,level);
points(:,2)=pointsCantorSet(numpoints,level);

%scatter(points(:,1),points(:,2),'.')