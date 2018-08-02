function  points = pointsDiskAreaOne(numpoints)
% Samples numpoints points uniformly at random from the disk of area one in
% the plane centered at the origin. This disk has radius 1/sqrt(pi).

i=0;
points=zeros(numpoints,2);
while i<numpoints
    point = 2*rand(1,2)/sqrt(pi)-1/sqrt(pi);
    if norm(point)<=1/sqrt(pi)
        i=i+1;
        points(i,:)=point;
    end
end

% scatter(points(:,1),points(:,2),'.')