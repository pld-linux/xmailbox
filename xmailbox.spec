Summary: An X Window System utility which notifies you of new mail.
Name: xmailbox
Version: 2.5
Release: 7
Copyright: MIT
Group: Applications/Internet
Source: ftp://ftp.x.org/contrib/applications/xmailbox-2.5.tar.gz
Patch1: xmailbox-2.2-xpm.patch
Patch2: xmailbox-2.4-glibc.patch
BuildRoot: /var/tmp/xmailbox-root

%description
The xmailbox program is an X Window System program which notifies you
when mail arrives.  Xmailbox is similar to the xbiff program, but it
offers more features and notification options.

Install the xmailbox package if you'd like a graphical program for X
which will notify you when new mail arrives.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
xmkmf
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

strip xmailbox
make DESTDIR=$RPM_BUILD_ROOT install install.man

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xmailbox <<EOF
xmailbox name "xmailbox"
xmailbox description "xmailbox"
xmailbox group Utilities/Mail
xmailbox exec "xmailbox &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/bin/xmailbox
/usr/X11R6/man/man1/xmailbox.1x
%config /usr/X11R6/lib/X11/app-defaults/XMailbox
%config /etc/X11/wmconfig/xmailbox
