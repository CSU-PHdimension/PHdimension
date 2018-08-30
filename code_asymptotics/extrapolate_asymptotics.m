function [varargout] = extrapolate_asymptotics(xv,yv,flag)
%
% function [varargout] = extrapolate_asymptotics(xv,yv)
%
%   This code is written to get a better understanding of 
%   asymptotic behavior in sequences with noise, 
%   assuming that there is an underlying
%   asymptotic scaling law y~c*x^alpha for x \to \infty,
%   and the inputs (xv,yv) are experimental samplings which have 
%   this underlying relationship. 
%
%   A simple log-transform and linear fit on all the data may not give a 
%   good result because may use data outside the asymptotic regime. This 
%   code tries to get around this problem automatically by examining a 
%   sequence of coefficient fits and inferring their limiting behavior 
%   assuming they behave "nicely" for x \to \infty. See code for details.
%
%   This code could be further extended by looking at a "second order" 
%   analysis, where the 
%
%   Manuchehr Aminian
%   6 February 2018
%
% Inputs: 
%           Vector xv, dimension n, with monotone increasing elements
%           Vector yv, dimension n
%           logical flag, whether to output "everything". (optional)
%                   Default: false.
%
%                   If false, one or two scalar outputs are given; 
%                       first alpha, then c (if asked for).
%                   If true, a cell output which has a sequence of
%                       fits, a list of the first index used in each fit, 
%                       and the fit values.
%               
% Outputs: 
%           varargout. The type depends on the optional input flag; 
%               see below for examples. Defaults to a vector size 2 with 
%               the fit parameters.
%
%
% Examples:
%
%   xv = 1:1000;
%   yv = xv + xv.^2 + randn(size(xv));
%   alpha = extrapolate_asymptotics(xv,yv)
%
%   xv = 1:1000;
%   yv = xv + 3*xv.^0.5 + randn(size(xv));
%   [alpha,c] = extrapolate_asymptotics(xv,yv)
%
%   % This one isn't nearly as easy...
%   xv = 1:10000;
%   yv = 10*xv.^0.2 + 3*xv.^0.5 + randn(size(xv));
%   output = extrapolate_asymptotics(xv,yv,true)
%

% Default for "flag" is false.
if (nargin==2)
    flag=false;
end

n = length(xv);

% Unfortunately there are still a few hard-coded parameters...
polyorder = 2;  % Polynomial order used for fitting alpha and c. 
                % Should be low order (probably 3 at most).

                

% minlen = 2^floor(log2(n*(2^-7)));    % smallest allowed number of points for a fit.
% minlen = min( max(minlen, 64), n);

% Geometric sequence of start points for sequence fits.
% Smallest subset is n-minlen+1:n; largest is 1:n. Scaling is done 
% in powers of two times minlen until 1:n is reached.
% powmax = floor(log2(n/minlen));
% startpts = n-minlen*2.^(powmax:-1:0)+1;

% startpts = [1, startpts];

startpts = 1:(n-polyorder-1);

fitsc = zeros(size(startpts));
fitsa = zeros(size(startpts));

logx = log(xv);
logy = log(yv);

% Get a sequence of fit coefficients c and alpha.
for i=1:length(startpts)
    sp = startpts(i);
    
    P = polyfit( logx(sp:end), logy(sp:end), 1 );
    fitsc(i) = exp( P(2) );
    fitsa(i) = P(1);
end

% Extrapolate the limit of the sequence as 
% x \to \infty by inferring that there is a function f(z), z=1/x, 
% which is analytic at f(0), which describes the fit coefficients 
% depending on the start of the tail of the sequence. 
% Given this, use a polynomial fit of the sequence and evaluate at z=0 
% for the final interpolation.

xseq = (xv(startpts));
zseq = 1./xseq;
Pc = polyfit( zseq, fitsc, polyorder );
Pa = polyfit( zseq, fitsa, polyorder );

c_final = polyval(Pc, 0);
alpha_final = polyval(Pa, 0);


if flag
    % This may change later.
    sout = struct;
    sout.startpts = startpts;
    sout.num_pts_used = n - startpts + 1;
    sout.cs = fitsc;
    sout.alphas = fitsa;
    sout.c_final = c_final;
    sout.alpha_final = alpha_final;
    
    varargout{1} = sout;
else
    % Give only the value of alpha
    varargout{1} = alpha_final;
    if nargout>1
        % Give the value of c as well..
        varargout{2} = c_final;
    end
    
end

return