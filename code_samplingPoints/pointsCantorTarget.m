function  [points,npoints] = pointsCantorTarget(numpoints,level,forcepoweroftwo)
% Samples points from the "Cantor Target". More precisely, samples points from
% the left endpoints (equivalently the midpoints, after a translation) of
% the intervals in the Cantor set at a specified level, then rotate around
% a circle. This distribution of points has dimension 1+log_3(2).

% Get points in Cantor set:
cantor=pointsCantorSet(numpoints,level);

% Sample angles uniformly from [0,2pi], with number of points linearly 
% proportional to radius:
n=round(numpoints*cantor(1))
angles=2*pi*rand(n,1);
x=cantor(1)*cos(angles);
y=cantor(1)*sin(angles);
for i = 2:numpoints
    n=round(numpoints*cantor(i))
    angles=2*pi*rand(n,1);
    x=cat(1,x,cantor(i)*cos(angles));
    y=cat(1,y,cantor(i)*sin(angles));
end

% Optionally truncate to the nearest power of 2 points.
if forcepoweroftwo
    n=2^floor(log2(length(x)));
    x=x(1:n); y=y(1:n);
end

% scatter(x,y,'o');
points=[x,y];
npoints=length(points);
