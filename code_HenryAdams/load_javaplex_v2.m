cfolder=pwd;

% You may need to change this depending on where your 
% matlab_examples folder is relative to this script.
javaplex_loc = '../../matlab_examples';

cd(javaplex_loc)


% These are the contents of 
% load_javaplex.m. Pasted here so that 
% we can skip the 'clc; clear all; close all' 
% statement in the original version.

javaaddpath('./lib/javaplex.jar');
import edu.stanford.math.plex4.*;

javaaddpath('./lib/plex-viewer.jar');
import edu.stanford.math.plex_viewer.*;

cd './utility';
addpath(pwd);
cd '..';

import edu.stanford.math.plex4.*;

disp('Javaplex loaded.')

% Go back to the original directory this 
% script was run from.
cd(cfolder)
