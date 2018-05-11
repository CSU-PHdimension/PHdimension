function plotStepFunction(values,yAxisMax)
% This function plots a step function, reparametrized so that the x
% coordinates vary from 0 to 1.
%   - values is a horizontal vector of all the heights of the step function.
%   - yAxisMax is the maximum height displayed on the y axis.

% Replace all values bigger than yAxisMax with yAxisMax.
values(values>yAxisMax)=yAxisMax;
n=length(values);
figure
% The last function value is repeated so that the last stair in the step function is plotted.
stairs((0:n)/n,[values,values(n)]);
xlim([0,1])
ylim([0,yAxisMax])

end

