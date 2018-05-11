function  points = pointsSierpinski2Dseparation(numpoints,level,sep)
% Samples points from the Sierpinski triangle. More precisely, samples points 
% from the bottom left endpoints of the triangles in the Sierpinski triangle
% at a specified level.

points=zeros(numpoints,2);
binarySequences=randi(3,numpoints,level)-1;
for i=1:level
    points=points+(binarySequences(:,i)==1)*[1,0]/((2+sep)^i)+(binarySequences(:,i)==2)*[1/2,sqrt(3)/2]/((2+sep)^i);
end

scatter(points(:,1),points(:,2),'.')