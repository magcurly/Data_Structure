#!/usr/bin/perl -w
use warnings;
use strict;
my @res;
sub out{
    my ($li,$n)=@_;
    my $m=$#$li;
    for(my $i=$m;$i>$n-2;$i--){
        push @res,$$li[$i];
        pop @$li;
        if($n-1>0){
            &out(\@$li,$n-1);
        }else{
            print join("\t",@res),"\n";
        }
        pop @res;
    }
}

my @test=[1,2,3,4,5];
&out(\@test,5)