Summary:	An X Window System utility which notifies you of new mail
Summary(cs.UTF-8):   Upozornní na píchod nové poty v prostedí X Window System
Summary(da.UTF-8):   Et systemvrktj for notificering ved ny e-post under X vinduessystemet
Summary(de.UTF-8):   Ein X Window System-Dienstprogramm, das Ihnen neue Post meldet
Summary(es.UTF-8):   Utilidad para X Window que notifica de la llegada de correo
Summary(fr.UTF-8):   Utilitaire pour le systme X Window qui vous informe de l'arrivée de nouveaux messages
Summary(id.UTF-8):   Utility X Window System yang memberitahukan jika ada surat baru
Summary(is.UTF-8):   X hjálparforrit sem tilkynnir þér þegar nýr póstur berst
Summary(it.UTF-8):   Utility per X Window che notifica l'arrivo di nuove mail
Summary(ja.UTF-8):   新着メールを通知する X Window System ユーティリティ
Summary(ko.UTF-8):   새 메일을 통지해주는 X 윈도우 시스템 유틸리티
Summary(nb.UTF-8):   Et systemverktøy for notifisering ved ny e-post under X vindusystemet
Summary(pl.UTF-8):   Narzędzie pod X powiadamiające o nowej poczcie
Summary(pt.UTF-8):   Um utilitário do X Window System que o notifica do 'e-mail' novo
Summary(ru.UTF-8):   Утилита для извещения о получении новой почты в X Window System
Summary(sk.UTF-8):   Nástroj pre systém X Window, ktorá vás upozorňuje na novú poštu
Summary(sl.UTF-8):   Pripomoček, ki vas v Oknih X opozori na novo pošto
Summary(sv.UTF-8):   Ett verktyg under X11 som meddelar när du fått ny post
Summary(zh_CN.UTF-8):   一个通知你新到邮件的 X 窗口系统工具。
Name:		xmailbox
Version:	2.5
Release:	16
License:	MIT
Group:		Applications/Mail
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
# Source0-md5:	31ac48e470724267ec00f8f93ccf22af
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:		%{name}-xpm.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-main-returntype.patch
Patch4:		%{name}-PLD.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xmailbox program is an X Window System program which notifies you
when mail arrives. Xmailbox is similar to the xbiff program, but it
offers more features and notification options.

%description -l cs.UTF-8
Xmailbox je program pro X Window System, který vás upozorní,
kdy vám pijde nová elektronická pota. Xmailbox je podobný programu
xbiff program, avak mete si vybrat z více moností upozornní.

%description -l da.UTF-8
Programmet xmailbox er et X-program som meddeler dig nr der
kommer post. Xmailbox ligner programmet xbiff, men det tilbyder flere
finesser og valgmuligheder.

%description -l de.UTF-8
Das Programm xmailbox ist ein X Window System-Programm, das Sie
benachrichtigt, wenn Mails eingehen. Es ähnelt dem Programm xbiff,
bietet jedoch mehr Funktionen und Benachrichtigungsoptionen.

%description -l es.UTF-8
El programa xmailbox es un programa para X Window que notifica de
la llegada de nuevo correo. Xmailbox es similar al programa xbiff, pero
proporciona más funciones y opciones de notificación.

%description -l fr.UTF-8
Le programme xmailbox est un programme pour le systme X Window qui vous
informe de l'arrivée de nouveaux messages. Xmailbox est semblable au
programme xbiff, mais il offre plus de fonctions et d'options de
notification.

%description -l id.UTF-8
Program xmailbox adalah program X Window System yang memberitahukan anda
jika ada surat baru yang datang.  Xmailbox mirip dengan program xbiff,
tetapi memiliki kemampuan lainnya dan memiliki notification option.

%description -l is.UTF-8
Xmailbox forriti er X gluggakerfisforrit sem ltur ig vita egar
póstur berst.  Xmailbox svipar til forritsins xbiff, nema a býur
upp á meiri möguleika og fjölbreyttari tilkynningar.

%description -l it.UTF-8
Il programma xmailbox  un programma per X Window che segnala
le mail quando arrivano. Xmailbox simile al programma xbiff, ma offre
pi funzionalit e opzioni per la notifica."

%description -l ja.UTF-8
xmailbox プログラムはメールの着信を通知する X Window System プログラムです。
xmailbox は、xbiff プログラムと似ていますがより多くの機能と通知オプションを
提供しています。

%description -l pl.UTF-8
xmailbox jest programem pod X Window System powiadamiający o nadejściu
poczty. Jest podobny do programu xbiff, lecz oferuje więcej możliwości
i opcji powiadomienia.

%description -l pt.UTF-8
O programa xmailbox é um programa do X Window System que o notifica
quando chega 'e-mail'. o xmailbox é parecido com o xbiff, mas oferece
mais capacidades e opções de notificação.

%description -l ru.UTF-8
Программа xmailbox - это программа для X Window System, которая извещает
о получении новой почты. Xmailbox похожа на программу xbiff, но она
имеет больше возможностей и опций.

%description -l sk.UTF-8
Program xmailbox pre systém X Window vás upozorňuje na príchod
novej pošty. Xmailbox je podobný programu xbiff, ale ponúka
viac možností a volieb na upozornenie.

%description -l sv.UTF-8
Programmet xmailbox går under X11 och meddelar dig när det
kommer post.  Xmailbox liknar programmet xbiff, men det erbjuder fler
finesser och valmöjligheter.

%description -l zh_CN.UTF-8
xmailbox 程序是一种在邮件到达时向您发出通知的 X Window 系统程序。
Xmailbox 类似于 xbiff 程序，但是提供了更多的功能和通知选项。

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{icons,sounds}

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail/xmailbox.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install *.xpm icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install *.au $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xmailbox
%{_mandir}/man1/xmailbox.1x*
%config %{_libdir}/X11/app-defaults/XMailbox
%{_applnkdir}/Network/Mail/xmailbox.desktop
%{_datadir}/%{name}/icons/*
%{_datadir}/%{name}/sounds/*
%{_pixmapsdir}/xmailbox.png
