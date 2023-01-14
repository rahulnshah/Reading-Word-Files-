#!/usr/bin/perl
use strict;
use warnings;

# if a test_scripts folder does not exist make one
my $permissions = "0755";
if(!(-e "test_scripts"))
{
	mkdir "test_scripts", oct($permissions) or die "cannot create test_scripts: $!";
}
# if a faild_script_msgs folder does not exist, make one
if(!(-e "failed_test_scripts_msgs"))
{
	mkdir "failed_test_scripts_msgs", oct($permissions) or die "cannot create failed_test_scripts_msgs: $!";
}
# move all generated text files into the test_scripts folder
foreach my $file (<*.txt>)
{
	# if the file is not "req...s.txt
	if($file =~ /(\w+)\./ && $1 ne "requirements")
	{
		# move $file into test_scripts  
		rename "$file", "test_scripts/$1.py";
	}
}
# Run every script, if one fails, save the error description into a text file and save it in a folder called failed_script_msgs

