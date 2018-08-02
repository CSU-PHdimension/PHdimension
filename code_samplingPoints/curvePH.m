function curvePH(numpoints)
import edu.stanford.math.plex4.*;

% This code computes the persistent homology barcodes from a random sampling of points from various metric spaces. It relies on the Javaplex software package (http://appliedtopology.github.io/javaplex/)

disp('Sampling points...')

max_dimension = 0;
max_filtration_value = 7 / numpoints
point_cloud = rand(numpoints,1);
name = ['Interval-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 0;
% max_filtration_value = 2 / sqrt(numpoints);
% point_cloud = rand(numpoints,2); % points on square
% name = ['Square-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 1;
% max_filtration_value = 3 / sqrt(numpoints);
% point_cloud = rand(numpoints,2);
% name = ['Square-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 1;
% max_filtration_value = 3 / sqrt(numpoints);
% point_cloud = pointsDiskAreaOne(numpoints);
% name = ['Disk-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 1;
% max_filtration_value = 3 / sqrt(numpoints);
% point_cloud = pointsTriangleAreaOne(numpoints);
% name = ['Triangle-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 2;
% max_filtration_value = 2 / numpoints^(1/3);
% point_cloud = rand(numpoints,3);
% name = ['Cube-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 0;
% max_filtration_value = 200 / numpoints^(log(3)/log(2));
% level = 100000;
% point_cloud = pointsCantorSet(numpoints,level);
% name = ['Cantor-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 1;
% max_filtration_value = 10 / numpoints^(log(3)/log(4));
% level = 100000;
% point_cloud = pointsCantorDust2D(numpoints,level);
% name = ['CantorDust2D-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 2;
% max_filtration_value = 4 / numpoints^(log(3)/log(8));
% level = 100000;
% point_cloud = pointsCantorDust3D(numpoints,level);
% name = ['CantorDust3D-',int2str(max_dimension),'-',int2str(numpoints)];

% max_dimension = 1;
% max_filtration_value = 10 / numpoints^(log(2)/log(3));
% level = 100000;
% point_cloud = pointsSierpinski2D(numpoints,level);
% name = ['Sierpinski2D-',int2str(max_dimension),'-',int2str(numpoints)];

disp('Computing barcodes...')
num_divisions = 10000000;

% Putting in some try/catch statements to automatically load javaplex 
% if the user hasn't already.
try
    stream = api.Plex4.createVietorisRipsStream(point_cloud, max_dimension+1, max_filtration_value, num_divisions);
catch
    try
        run load_javaplex_v2.m
        stream = api.Plex4.createVietorisRipsStream(point_cloud, max_dimension+1, max_filtration_value, num_divisions);
    catch
        disp('Unable to load Javaplex. Check to see if load_javaplex_v2 points to the right directory.')
        return
    end
end

% TODO: print size
persistence = api.Plex4.getModularSimplicialAlgorithm(max_dimension+1, 2);
intervals = persistence.computeIntervals(stream);
% NEXT: do for loop over homological dimensions.

for i=0:max_dimension
    intervalsMatrix = edu.stanford.math.plex4.homology.barcodes.BarcodeUtility.getEndpoints(intervals,i,0);
    if i==0
        values = sort(intervalsMatrix(:,2))';
    else
        % persistence
        values = sort(intervalsMatrix(:,2)-intervalsMatrix(:,1))';
        % birth
        % values = sort(intervalsMatrix(:,1))';
        % death
        % values = sort(intervalsMatrix(:,2))';
        % size
        % values = sort((intervalsMatrix(:,2)+intervalsMatrix(:,1))/2)';
    end
    plotStepFunction(values,max_filtration_value);
end

% options.filename = name;
% options.max_filtration_value = max_filtration_value;
% options.max_dimension = max_dimension;
% plot_barcodes(intervals, options);