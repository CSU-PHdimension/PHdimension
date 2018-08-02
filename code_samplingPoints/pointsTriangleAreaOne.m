function  points = pointsTriangleAreaOne(numpoints)
% Samples numpoints points uniformly at random from an equilateral
% triangle of area one in the plane. An equilateral triangle with
% side-length a has area sqrt(3)/4*a^2 altitude sqrt(3)/2*a, and hence the
% triangle I want has side-length 2*3^(-1/4) and altitude 3^(1/4). I chose
% the triangle with coordinates (-3^(1/4),0),(3^(1/4),0), and (0,3^(1/4)).
% The constraint for the bottom of this triangle is given when choosing
% points in the square, and the constraints for the top edges of this
% triangle are given by the inequalities in the rejection sampling.

i=0;
points=zeros(numpoints,2);
while i<numpoints
    point = 2*rand(1,2)*3^(-1/4)-[3^(-1/4),0];
    if point(2)<=-sqrt(3)*point(1)+3^(1/4) && point(2)<=sqrt(3)*point(1)+3^(1/4)
        i=i+1;
        points(i,:)=point;
    end
end

% scatter(points(:,1),points(:,2),'.')