#!/usr/bin/perl
use strict;
use warnings;

# change into the specified directory
my $dir = "test_scripts";

chdir( $dir ) or die "Couldn't go inside $dir directory, $!";

# convert all generated text files into python files in the test_scripts folder
foreach my $file (<*.txt>)
{
	# if the file is not "req...s.txt
	if($file =~ /(\w+)\./ && $1 ne "requirements")
	{
		# move $file into test_scripts  
		rename "$file", "$1.py";
	}
}
# Run every script, if one fails, save the error description into a text file and save it in a folder called failed_script_msgs

