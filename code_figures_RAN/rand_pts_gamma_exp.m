for i=1:100
    x=rand(5000,2);
    X(i).x=x
    [h1,h0]=rca1pc(x,.06); 
    X(i).h0=h0; 
    X(i).h1=h1; 
end
save('5000randpts','X')
%Try to fit distributions for H1: (take 100 trials with 5000 points each)   
H1_barlengths=[]; 
for i=1:100
H1_barlengths=[H1_barlengths; X(i).h1(:,2)-X(i).h1(:,1)]; 
end 
H1_barlengths=H1_barlengths*5000^0.5; 
H1_death=[]; 
for i=1:10
H1_death=[H1_death; X(i).h1(:,2)]; 
end 
H1_death=H1_death*5000^0.5; 
% use distribution fitter 
%note: gamma distributions seem to fit both pretty well -- with different
%shape parameters, of course
%% Plot PH functions with errorbars: 
  t=0:0.005:1; 
  data0=zeros(100,size(t,2));
  for i=1:100
        int= X(i).h0(1:end-1,:); 
        f=plotflipBC(int*(5000)^0.5, 'barlength');
        data0(i,:)=ppval(f,t);
  end

  fh0=mean(data0);
  ferr=std(data0);
  clf
  shadedErrorBar(t,reshape(fh0,1,[]),reshape(ferr, 1,[]))
 
  
  
  data1=zeros(100,size(t,2));
  data2=zeros(100,size(t,2));
  data3=zeros(100,size(t,2));
  for i=1:100
        int= X(i).h1(1:end-1,:); 
        f1=plotflipBC(int*(5000)^0.5, 'barlength', 'red');
        data1(i,:)=ppval(f1,t);
        f2=plotflipBC(int*(5000)^0.5, 'birth');
        data2(i,:)=ppval(f2,t);
        f3=plotflipBC(int*(5000)^0.5, 'death');
        data3(i,:)=ppval(f3,t);       
  end
  fh1=mean(data1);  ferr1=std(data1); 
  fh2=mean(data2);  ferr2=std(data2);  
  fh3=mean(data3);  ferr3=std(data3);
  clf
  shadedErrorBar(t,reshape(fh1,1,[]),reshape(ferr1, 1,[]))
  hold on; 
  shadedErrorBar(t,reshape(fh2,1,[]),reshape(ferr2, 1,[]))
  shadedErrorBar(t,reshape(fh3,1,[]),reshape(ferr3, 1,[]))

  shadedErrorBar(t,reshape(fh0,1,[]),reshape(ferr, 1,[]))



%% Now lets see if there is a trend in parameters as the number of points increases (is there a trend?) 

for i=1:51
    for j=1:25
        x=rand(900+i*100,2);
        X{i,j,1}=x;
        [I1,I0]=rca1pc(x,.15-i*.001);
        X{i,j,2}=I0;
        X{i,j,3}= I1;
        pd=fitdist(I1(:,1)*(900+i*100)^0.5, 'Gamma');
        X{i,j,4}=pd;
        X{i,j,5}=gamlike([pd.a, pd.b], I1(:,1)*(900+i*100)^0.5);
        pd=fitdist(I1(:,2)*(900+i*100)^0.5, 'Gamma');
        X{i,j,6}=pd;
        X{i,j,7}=gamlike([pd.a, pd.b], I1(:,2)*(900+i*100)^0.5);
        pd=fitdist((I1(:,2)-I1(:,1))*(900+i*100)^0.5, 'Gamma');
        X{i,j,8}=pd;
        X{i,j,9}=gamlike([pd.a, pd.b],(I1(:,2)-I1(:,1))*(900+i*100)^0.5);
    end
end
save('rand_pts_withH1gamma', 'X', '-v7.3')
for i=1:51
    for j=1:25
    pd=X{i,j,8};
    err=paramci(pd); 
    a(i,j)=pd.a; 
    err_a(i,j)=err(2,1)-err(1,1);  
    b(i,j)=pd.b; 
    err_b(i,j)=err(2,2)-err(1,2); 
    end
end
errorbar(mean(a'),mean(err_a'))
 hold on; errorbar(mean(b'),mean(err_b'))
 
 for i=1:51
     for j=1:25
         LL(i,j)=X{i,j,5};
     end
 end

errorbar(mean(LL'), std(LL'))
 
% do the curve seem to converge as n increases (yes! scale by n^1/d)

 for i=1:51
     j=mod(i,7)+1; 
     int= X{i,1,2}(1:end-1,:); 
    hold on;  plotflipBC(int*(900+i*100)^0.5, 'barlength', co(j,:)); 
     pause
 end

  for i=1:51
     j=mod(i,7)+1; 
     int= X{i,1,3}(1:end-1,:); 
    hold on;  plotflipBC(int*(900+i*100)^0.5, 'barlength', co(j,:)); 
     pause
  end
  
  %
 
 %% mean and error bars 
  t=0:0.01:1; 
  data0=zeros(51,25,size(t,2));
  for i=1:51
    for j=1:25
        int= X{i,j,2}(1:end-1,:); 
        f=plotflipBC(int*(900+i*100)^0.5, 'barlength');
        data0(i,j,:)=ppval(f,t);
           end
  end

  fh0=mean(mean(data0));
  ferr=std(std(data0));
  clf
  shadedErrorBar(t,reshape(fh0,1,[]),reshape(ferr, 1,[]))
  
data1=zeros(51,25,size(t,2));
  
for i=1:51
    for j=1:25
        int= X{i,j,3}; 
        f=plotflipBC(int*(900+i*100)^0.5, 'barlength');
        data1(i,j,:)=ppval(f,t);
           end
  end
  fh1=mean(mean(data1));
  ferr1=std(std(data1));
  clf
  shadedErrorBar(t,reshape(fh1,1,[]),reshape(ferr1, 1,[]))
  

  for i=1:51
    for j=1:25
        int= X{i,j,3}; 
        f=plotflipBC(int*(900+i*100)^0.5, 'birth');
        data2(i,j,:)=ppval(f,t);
           end
end
  fh2=mean(mean(data2));
  ferr2=std(std(data2));
  clf
  shadedErrorBar(t,reshape(fh2,1,[]),reshape(ferr2, 1,[]))
  
for i=1:51
    for j=1:25
        int= X{i,j,3}; 
        f=plotflipBC(int*(900+i*100)^0.5, 'death');
        data3(i,j,:)=ppval(f,t);
           end
end
  fh3=mean(mean(data3));
  ferr3=std(std(data3));
  clf
  shadedErrorBar(t,reshape(fh3,1,[]),reshape(ferr3, 1,[]))
 
  
  
  
  
  
  
  
  %%%%%%%%%%
  
  
  
  
  
  for i=1:51
     j=mod(i,7)+1; 
     int= X{i,1,3}(1:end-1,:); 
    hold on;  plotflipBC(int*(900+i*100)^0.5, 'barlength', co(j,:)); 
     pause
  end
 
 %try to fit H1 bar lenghts
 t=0:0.0005:1; 
 i=51; 
 int=X{i,1,3}(1:end-1,:);
 f=plotflipBC(int*(900+i*100)^0.5, 'barlength'); 
 data=ppval(f,t);
 
 ft=fit(t,data,'-1*a*t^b*log(1-t)')
 
hold on; 

%%
%grow set by adding in 100 points 
x=rand(100,2); 
X(1).x=x; 
[h1,h0]=rca1pc(x,.3); 
X(i).h0=h0; 
X(i).h1=h1; 

for i=2:100
    x_new=rand(100,2);
    x=[x;x_new];
    X(i).x=x; 
    [h1,h0]=rca1pc(x,.3-.0024*i); 
    X(i).h0=h0; 
    X(i).h1=h1; 
end

t=0:0.005:1; 
  data0=zeros(100,size(t,2));
  for i=1:100
        int= X(i).h0(1:end-1,:); 
        f=plotflipBC(int*(100*i)^0.5, 'barlength');
        data0(i,:)=ppval(f,t);
  end

  fh0=mean(data0);
  ferr=std(data0);
  clf
  shadedErrorBar(t,reshape(fh0,1,[]),reshape(ferr, 1,[]))
 
  
  data1=zeros(100,size(t,2));  data2=zeros(100,size(t,2));  data3=zeros(100,size(t,2));
  for i=1:100
        int= X(i).h1(1:end-1,:); 
        f1=plotflipBC(int*(100*i)^0.5, 'barlength', 'red');
        data1(i,:)=ppval(f1,t);
        f2=plotflipBC(int*(100*i)^0.5, 'birth');
        data2(i,:)=ppval(f2,t);
        f3=plotflipBC(int*(100*i)^0.5, 'death');
        data3(i,:)=ppval(f3,t);       
  end
  fh1=mean(data1);  ferr1=std(data1); 
  fh2=mean(data2);  ferr2=std(data2);  
  fh3=mean(data3);  ferr3=std(data3);
  clf
  shadedErrorBar(t,reshape(fh1,1,[]),reshape(ferr1, 1,[]))
  hold on; 
  shadedErrorBar(t,reshape(fh2,1,[]),reshape(ferr2, 1,[]))
  shadedErrorBar(t,reshape(fh3,1,[]),reshape(ferr3, 1,[]))

  shadedErrorBar(t,reshape(fh0,1,[]),reshape(ferr, 1,[]))
