Summary:	An X Window System utility which notifies you of new mail
Summary(cs):	Upozornní na píchod nové poty v prostedí X Window System
Summary(da):	Et systemvrktj for notificering ved ny e-post under X vinduessystemet
Summary(de):	Ein X Window System-Dienstprogramm, das Ihnen neue Post meldet
Summary(es):	Utilidad para X Window que notifica de la llegada de correo
Summary(fr):	Utilitaire pour le systme X Window qui vous informe de l'arrivée de nouveaux messages
Summary(id):	Utility X Window System yang memberitahukan jika ada surat baru
Summary(is):	X hjálparforrit sem tilkynnir şér şegar nır póstur berst
Summary(it):	Utility per X Window che notifica l'arrivo di nuove mail
Summary(ja):	¿·Ãå¥á¡¼¥ë¤òÄÌÃÎ¤¹¤ë X Window System ¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(ko):	»õ ¸ŞÀÏÀ» ÅëÁöÇØÁÖ´Â X À©µµ¿ì ½Ã½ºÅÛ À¯Æ¿¸®Æ¼
Summary(no):	Et systemverktøy for notifisering ved ny e-post under X vindusystemet
Summary(pl):	Narzêdzie pod X powiadamiaj±ce o nowej poczcie
Summary(pt):	Um utilitário do X Window System que o notifica do 'e-mail' novo
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ÉÚ×ÅİÅÎÉÑ Ï ĞÏÌÕŞÅÎÉÉ ÎÏ×ÏÊ ĞÏŞÔÙ × X Window System
Summary(sk):	Nástroj pre systém X Window, ktorá vás upozoròuje na novú po¹tu
Summary(sl):	Pripomoèek, ki vas v Oknih X opozori na novo po¹to
Summary(sv):	Ett verktyg under X11 som meddelar när du fått ny post
Summary(zh_CN):	Ò»¸öÍ¨ÖªÄãĞÂµ½ÓÊ¼şµÄ X ´°¿ÚÏµÍ³¹¤¾ß¡£
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

%description -l cs
Xmailbox je program pro X Window System, kterı vás upozorní,
kdy vám pijde nová elektronická pota. Xmailbox je podobnı programu
xbiff program, avak mete si vybrat z více moností upozornní.

%description -l da
Programmet xmailbox er et X-program som meddeler dig nr der
kommer post. Xmailbox ligner programmet xbiff, men det tilbyder flere
finesser og valgmuligheder.

%description -l de
Das Programm xmailbox ist ein X Window System-Programm, das Sie
benachrichtigt, wenn Mails eingehen. Es ähnelt dem Programm xbiff,
bietet jedoch mehr Funktionen und Benachrichtigungsoptionen.

%description -l es
El programa xmailbox es un programa para X Window que notifica de
la llegada de nuevo correo. Xmailbox es similar al programa xbiff, pero
proporciona más funciones y opciones de notificación.

%description -l fr
Le programme xmailbox est un programme pour le systme X Window qui vous
informe de l'arrivée de nouveaux messages. Xmailbox est semblable au
programme xbiff, mais il offre plus de fonctions et d'options de
notification.

%description -l id
Program xmailbox adalah program X Window System yang memberitahukan anda
jika ada surat baru yang datang.  Xmailbox mirip dengan program xbiff,
tetapi memiliki kemampuan lainnya dan memiliki notification option.

%description -l is
Xmailbox forriti er X gluggakerfisforrit sem ltur ig vita egar
póstur berst.  Xmailbox svipar til forritsins xbiff, nema a bıur
upp á meiri möguleika og fjölbreyttari tilkynningar.

%description -l it
Il programma xmailbox  un programma per X Window che segnala
le mail quando arrivano. Xmailbox simile al programma xbiff, ma offre
pi funzionalit e opzioni per la notifica."

%description -l ja
xmailbox ¥×¥í¥°¥é¥à¤Ï¥á¡¼¥ë¤ÎÃå¿®¤òÄÌÃÎ¤¹¤ë X Window System ¥×¥í¥°¥é¥à¤Ç¤¹¡£
xmailbox ¤Ï¡¢xbiff ¥×¥í¥°¥é¥à¤È»÷¤Æ¤¤¤Ş¤¹¤¬¤è¤êÂ¿¤¯¤Îµ¡Ç½¤ÈÄÌÃÎ¥ª¥×¥·¥ç¥ó¤ò
Äó¶¡¤·¤Æ¤¤¤Ş¤¹¡£

%description -l pl
xmailbox jest programem pod X Window System powiadamiaj±cy o nadej¶ciu
poczty. Jest podobny do programu xbiff, lecz oferuje wiêcej mo¿liwo¶ci
i opcji powiadomienia.

%description -l pt
O programa xmailbox é um programa do X Window System que o notifica
quando chega 'e-mail'. o xmailbox é parecido com o xbiff, mas oferece
mais capacidades e opções de notificação.

%description -l ru
ğÒÏÇÒÁÍÍÁ xmailbox - ÜÔÏ ĞÒÏÇÒÁÍÍÁ ÄÌÑ X Window System, ËÏÔÏÒÁÑ ÉÚ×ÅİÁÅÔ
Ï ĞÏÌÕŞÅÎÉÉ ÎÏ×ÏÊ ĞÏŞÔÙ. Xmailbox ĞÏÈÏÖÁ ÎÁ ĞÒÏÇÒÁÍÍÕ xbiff, ÎÏ ÏÎÁ
ÉÍÅÅÔ ÂÏÌØÛÅ ×ÏÚÍÏÖÎÏÓÔÅÊ É ÏĞÃÉÊ.

%description -l sk
Program xmailbox pre systém X Window vás upozoròuje na príchod
novej po¹ty. Xmailbox je podobnı programu xbiff, ale ponúka
viac mo¾ností a volieb na upozornenie.

%description -l sv
Programmet xmailbox går under X11 och meddelar dig när det
kommer post.  Xmailbox liknar programmet xbiff, men det erbjuder fler
finesser och valmöjligheter.

%description -l zh_CN
xmailbox ³ÌĞòÊÇÒ»ÖÖÔÚÓÊ¼şµ½´ïÊ±ÏòÄú·¢³öÍ¨ÖªµÄ X Window ÏµÍ³³ÌĞò¡£
Xmailbox ÀàËÆÓÚ xbiff ³ÌĞò£¬µ«ÊÇÌá¹©ÁË¸ü¶àµÄ¹¦ÄÜºÍÍ¨ÖªÑ¡Ïî¡£

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
