jenkins practice
================

`Jenkins`_ is a powerful appication that allows continuous integration and
continuous delivery of projects, regardless of the platform you are working
on.

Start jenkins container
-----------------------

::

  docker run -d -p 49001:8080 -v ~/jenkins-volume:/var/jenkins_home:z -t jenkins





References:

.. _Jenkins: https://www.tutorialspoint.com/jenkins/index.htm
