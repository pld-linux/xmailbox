Summary:	An X Window System utility which notifies you of new mail
Name:		xmailbox
Version:	2.5
Release:	7
Copyright:	MIT
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplica��es/Correio Eletr�nico
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Patch1:		xmailbox-2.2-xpm.patch
Patch2:		xmailbox-2.4-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xmailbox program is an X Window System program which notifies you
when mail arrives. Xmailbox is similar to the xbiff program, but it
offers more features and notification options.

Install the xmailbox package if you'd like a graphical program for X
which will notify you when new mail arrives.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

make install install.man DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xmailbox <<EOF
xmailbox name "xmailbox"
xmailbox description "xmailbox"
xmailbox group Utilities/Mail
xmailbox exec "xmailbox &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/xmailbox
%{_mandir}/man1/xmailbox.1x.gz
%config %{_libdir}/X11/app-defaults/XMailbox
%config %{_sysconfdir}/X11/wmconfig/xmailbox
