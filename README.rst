jenkins practice
================

`Jenkins`_ is a powerful application that allows continuous integration and
continuous delivery of projects, regardless of the platform you are working
on.

`Start jenkins container`_
--------------------------
::

  docker run -dti -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins

After starting Jenkins, access http://host_ip:8080 to initiate and configure
Jenkins

Install jenkins-job-builder
---------------------------
::
  pip install --user jenkins-job-builder












.. _Jenkins: https://www.tutorialspoint.com/jenkins/index.htm
.. _Start jenkins container: https://github.com/jenkinsci/docker/blob/master/README.md
