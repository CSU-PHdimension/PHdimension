function  points = pointsSierpinski2D(numpoints,level)
% Samples points from the Sierpinski triangle. More precisely, samples points 
% from the bottom left endpoints of the triangles in the Sierpinski triangle
% at a specified level.

points=zeros(numpoints,2);
ternarySequences=randi(3,numpoints,level)-1;
for i=1:level
    points=points+(ternarySequences(:,i)==1)*[1,0]/(2^i)+(ternarySequences(:,i)==2)*[1/2,sqrt(3)/2]/(2^i);
end

scatter(points(:,1),points(:,2),'.')
