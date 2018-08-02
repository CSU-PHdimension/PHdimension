function ph_intervals = ripserToArray(filename,n)
% Opens the file specified by filename and returns an Nx2 array containing
% the birth and death times of the intervals in dimension dim.

% Verify that dim is a positive interger.
if n < 0 || floor(n) ~= n
    error('Invalid dimension');
end

% Load the ripser output text file.
text = fileread(filename);

% Parse the text file for occurences of "dim n" and "dim n+1" and store all
% text that occurs between them.
startstr = ['persistence intervals in dim ', int2str(n), ':', newline];
if n > 0
    endstr = [newline, 'persistence intervals in dim ', int2str(n+1), ':'];
else
    endstr = '[0, )';     % Remove the infinite interval in H_0
end
if contains(text,endstr)
    intervals = extractBetween(text,startstr,endstr);
else
    intervals = extractAfter(text,startstr);
end

% Remove interval delimiters.
intervals = regexprep(intervals,'[|)| ','');
% Convert to numerical array.
ph_intervals = str2num(char(intervals));