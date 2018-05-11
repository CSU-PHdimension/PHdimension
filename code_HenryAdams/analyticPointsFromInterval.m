function  functionValues = analyticPointsFromInterval(n)
% Comment written months later. Consider points randomly sampled from the
% unit interval [0,1]. I found the following analytic formula for the
% length of the i-th longest barcode, below. This curve tends to -log(1-x),
% if I remember correctly.
% TODO: Add more detail to these comments!
functionValues=zeros(n+1,1);
functionValues(1)=1/((n+1)*(n+1));
for k=1:n
    functionValues(k+1)=functionValues(k)+1/((n+1)*(n+1-k));
end
    

%scatter(points(:,1),points(:,2),'.')