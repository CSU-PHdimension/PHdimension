function  points = pointsCantorDust3D(numpoints,level)
% Samples points from the "3D Cantor Dust set", which is the Cartesian 
% product of three copies of the Cantor set. More precisely, samples points 
% from the left endpoints (equivalently the midpoints, after a translation)
% of the intervals in the Cantor set at a specified level, and then takes
% the ordered pair of three such random points.

points=zeros(numpoints,3);
points(:,1)=pointsCantorSet(numpoints,level);
points(:,2)=pointsCantorSet(numpoints,level);
points(:,3)=pointsCantorSet(numpoints,level);

%scatter3(points(:,1),points(:,2),points(:,3),'.')