sharevalue

Question:
----------
To print the latest price of the company whose NASDAQ symbol will be given in the command line

Solution:
---------
1. Modules are imported using the command import.

2. A function share is defined to get the latest share price of the company.

3. The link of the site to get the price is stored in a variable named
   share_link.

4. The site(stored in the variable share_link) returns the latest value of the     company by using the command urllib2.urlopen(share_link) and it is stored in    the variable share_value.

5. The share value of the company is being read by the command                     share_value.read() and is stored in the variable s.

6. The share value of the company is printed by the print command.

7. Then checking is made whether only one input is given or not in the command     line by the command if __name__=='__main__':

8. The program returns an error if more than one input is used.

Code
-----
The code is given here :- `link`_

.. _Link: https://github.com/PriyankaKotiyal/tasks_dgplug/blob/d99add8ba1d7047191e377ee3309f6dae1f39d79/sharevalue/sharevalue.py#L1

