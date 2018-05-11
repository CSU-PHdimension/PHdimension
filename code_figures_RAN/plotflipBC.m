function [pwftn] = plotflipBC( int,  opt, colorstr)
%plots the flipped barcode on the interval [0,1] as a step function, each
%step is a width of 1/n (n being the number of persistence points) 
%INPUTS: % opt: 'both' will plot the birth and death (as 2 functions) 
%       'birth' will plot sorted birth times
%       'death' will plot sorted death times
%       'barlength' will plot sorted barlength 
%       'both' will plot birth and death on same plot
%     int: persistence intervals
%     colorstr (optional): RGB color triple, useful for lines on same plot!
narginchk(1,3)
n=length(int); 
breaks=[0:1/n:1];

if strcmp(opt,'birth')
    coefs=sort(int(:,1));
elseif strcmp(opt,'death')
    coefs=sort(int(:,2));
elseif strcmp(opt,'barlength')
    coefs=sort(int(:,2)-int(:,1));
elseif strcmp(opt, 'both')
    coefs1=int(:,1);
    coefs2=int(:,2);
else
    coefs=int(:,2)-int(:,1);
end

if ~strcmp(opt, 'both')
    pwftn=mkpp(breaks, coefs);
    xx=0:1/n:1;
    %plot(xx,ppval(pwftn,xx))
    if nargin==2
        plot(xx,ppval(pwftn,xx),'Color', [0 .447 .741])
    else
        plot(xx,ppval(pwftn,xx),'Color', colorstr, 'Linewidth', 1.5)
    end
else
    pwftn1=mkpp(breaks, coefs1);
    pwftn2=mkpp(breaks, coefs2);
    
    xx=0:1/n:1;
    %plot(xx,ppval(pwftn,xx))
    if nargin==2
        plot(xx,ppval(pwftn1,xx),'Color', [0 .447 .741],'Linewidth', 1.5)
        hold on;
        plot(xx,ppval(pwftn2,xx),'Color', [0 .447 .741],'Linewidth', 1.5)
    else
        plot(xx,ppval(pwftn1,xx),'Color', colorstr,'Linewidth', 1.5)
        hold on;
        plot(xx,ppval(pwftn2,xx),'Color', colorstr,'Linewidth', 1.5)
    end
end

end

