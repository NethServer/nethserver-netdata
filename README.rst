==================
nethserver-netdata
==================

Basic configuration for netdata.
nethserver-cockpit package access netadata on ``http://localhost:19999``
and uses the data to graph system statistics.

Do not change listening port otherwise Cockpit will not be able to access netdata.

Configuration DB
================

Properties:

- ``Bind``: bind IP addess, default to ``localhost``
- ``Alarms``: can be ``enabled`` or ``disabled``. Default to ``disabled`` to avoid unwanted mail to root user

Example: ::

 netdata=service
    Alarms=disabled
    Bind=localhost
    TCPPort=19999
    access=
    status=enabled


Links
=====

* Offical netdata site: https://my-netdata.io/
