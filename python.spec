
%define py_ver         2.3
%define py_prefix      %{_prefix}
%define py_libdir      %{py_prefix}/lib/python%{py_ver}
%define py_incdir      %{_includedir}/python%{py_ver}
%define py_sitedir     %{py_libdir}/site-packages
%define py_dyndir      %{py_libdir}/lib-dynload
%define py_comp        ./python -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"
%define py_ocomp       ./python -O -c "import compileall; import sys; compileall.compile_dir(sys.argv[1], ddir=sys.argv[1][len('$RPM_BUILD_ROOT'):])"

Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-OberflДche
Summary(es):	Lenguaje script de alto nivel con interface X
Summary(fr):	Langage de script de tИs haut niveau avec interface X
Summary(pl):	Python - jЙzyk obiektowy wysokiego poziomu
Summary(pt_BR):	Linguagem de programaГЦo interpretada, orientada a objeto de alto nМvel
Summary(ru):	Язык программирования очень высокого уровня с X-интерфейсом
Summary(tr):	X arayЭzlЭ, yЭksek dЭzeyli, kabuk yorumlayЩcЩ dili
Summary(uk):	Мова програмування дуже високого р╕вня з X-╕нтерфейсом
Name:		python
Version:	%{py_ver}c2
Release:	0.1
License:	PSF
Group:		Applications
URL:		http://www.python.org/
Source0:	http://www.python.org/ftp/python/%{py_ver}/Python-%{version}.tgz
# Source0-md5:	022ed1d1db12822bc13f930bc19f079c
Source1:	http://www.python.org/ftp/python/doc/%{version}/html-%{version}.tar.bz2
# Source1-md5:	c4c35e85912e23898871b5cedc521f17
Patch0:		%{name}-readline.patch
Patch1:		%{name}-%{name}path.patch
Patch2:		%{name}-default_encoding.patch
Patch3:		%{name}-no_ndbm.patch
Patch4:		%{name}-ac_fixes.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	db-devel >= 4
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	expat-devel
BuildRequires:	gmp-devel => 4.0
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tcl-devel >= 8.4.3
BuildRequires:	tix-devel >= 1:8.1.4-4
BuildRequires:	tk-devel >= 8.4.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	%{name} = %{py_ver}
Obsoletes:	python-xml
Obsoletes:	python-intl
Obsoletes:	python-curses
Obsoletes:	python-gdbm
Obsoletes:	python-zlib
Obsoletes:	python2
Obsoletes:	python2-devel

%description
Python is an interpreted, interactive, object-oriented programming
language. It incorporates modules, exceptions, dynamic typing, very
high level dynamic data types, and classes. Python combines remarkable
power with very clear syntax. It has interfaces to many system calls
and libraries, as well as to various window systems, and is extensible
in C or C++. It is also usable as an extension language for
applications that need a programmable interface. Finally, Python is
portable: it runs on many brands of UNIX, on the Mac, and on PCs under
MS-DOS, Windows, Windows NT, and OS/2.

%description -l de
Python ist eine interpretierte, interaktive, objektorientierte
Programmiersprache, vergleichbar zu Tcl, Perl, Scheme oder Java.
Python enthДlt Module, Klassen, Exceptions, High-Level dynamische
Datentypen und dynamisches Typisieren. Python unterstЭtzt Interfaces
zu vielen Systemaufrufen und Libraries, sowie verschiedene
Fenstersysteme (X11, Motif, Tk, Mac und MFC)

Programmierer kЖnnen neue built-in-Module fЭr Python in C oder C++
schreiben. Python kann auch als Erweiterungssprache fЭr Applikationen
benutzt werden, die ein programmierbares Interface brauchen. Dieses
Paket enthДlt die meisten Standard-Python-Module, und Module zum
Ansprechen von Tix (Tk-widget set) und RPM.

%description -l es
Python es un lenguaje de scripts interpretado orientado a objetos.
Contiene soporte para carga dinАmica de objetos, clases, mСdulos y
excepciones.

Es sencillo adicionar interfaces para nuevos sistemas de biblioteca a
travИs de cСdigo C, tornando Python fАcil de usar en ambientes
articulares/ personalizados. Este paquete Python incluye la mayorМa de
los mСdulos padrСn Python, junto con mСdulos para crear interfaces
para el conjunto de componentes Tix para Tk y RPM.

%description -l fr
Python est un langage de script interprИtИ et orientИ objet. Il gХre
le chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles bibliothХques systХmes
avec du code C est simple, ce qui rend Python facile Ю utiliser dans
des configs personnalisИes.

Ce paquetage Python contient la plupart des modules Python standards,
ainsi que ceux permettant l'interfaГage avec les widgets Tix pour Tk
et RPM.

%description -l pl
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
jЙzykiem programowania. Jest modularny, obsЁuguje wyj╠tki, dynamiczne
typy, zaawansowane dynamiczne struktury danych i klasy. Python Ё╠czy w
sobie du©e mo©liwo╤ci i przejrzyst╠ skЁadniЙ. Posiada interfejsy do
wielu wywoЁaЯ systemowych i bibliotek, w tym rСwnie© do rС©nych
bibliotek okienkowych. Mo©liwo╤ci jego mo©na jeszcze rozszerzaФ
poprzez odpowiednie moduЁy pisane w C lub C++. Python mo©e byФ rСwnie©
u©yty jako element aplikacji, ktСrym potrzebny jest interpreter do
skryptСw. I wreszcie, Python jest wieloplatformowy, dziaЁa na wielu
odmianach UNIX-a, Macu oraz PC pod DOS-em, Windows, WindowsNT oraz
OS/2.

%description -l pt_BR
Python И uma linguagem de scripts interpretada orientada a objetos.
ContИm suporte para carga dinБmica de objetos, classes, mСdulos e
exceГУes. Adicionar interfaces para novos sistemas de biblioteca
atravИs de cСdigo C И simples, tornando Python fАcil de usar em
ambientes particulares/personalizados.

Este pacote Python inclui a maioria do mСdulos padrЦo Python, junto
com mСdulos para interfaceamento para o conjunto de componentes Tix
para Tk e RPM.

%description -l ru
Python - это интерпретируемый, объектно-ориентированный язык
программирования. Он поддерживает динамическую загрузку объектов,
классы, модули и обработку исключительных ситуаций (exceptions).
Простота добавления интерфейсов к новым системным библиотекам через
код на языке C делает Python хорошим выбором для использования в
специальных конфигурациях.

%description -l tr
Python, nesneye yЖnelik bir kabuk yorumlayЩcЩdЩr. Nesnelerin,
sЩnЩflarЩn, modЭllerin ve aykЩrЩ durumlarЩn dinamik yЭklenmelerine
destek verir. C koduyla birlikte kullanЩmЩ son derece kolaydЩr. Bu
paket, standart Python birimlerinin ГoПunun yanЩsЩra Tk ve RPM iГin
arayЭz birimlerini de iГerir.

%description -l uk
Python - це ╕нтерпретована, об'╓ктно-ор╕╓нтована мова програмування.
В╕н п╕дтриму╓ динам╕чну загрузку об'╓кт╕в, класи, модул╕ та обробку
виключних ситуац╕й (exceptions). Простота додавання ╕нтерфейс╕в для
нових системних б╕бл╕отек через код на мов╕ C робить Python добрим
вибором для використання в спец╕альних конф╕гурац╕ях.

%package libs
Summary:	Python library
Summary(pl):	Biblioteka jЙzyka Python
Group:		Libraries/Python
Provides:	%{name}-libs = %{py_ver}

%description libs
Python library.

%description libs -l pl
Biblioteka jЙzyka Python.

%package modules
Summary:	Python modules
Summary(pl):	ModuЁy jЙzyka Python
Group:		Libraries/Python
Provides:	%{name}-modules = %{py_ver}
Requires:	%{name} = %{version}
Obsoletes:	python-logging
Obsoletes:	python-xmlrpc <= 1.0.1

%description modules
Python modules.

%description modules -l pl
ModuЁy jЙzyka Python.

%package pydoc
Summary:	Python interactive module documentation access support
Summary(pl):	Interaktywne korzystanie z dokumentacji moduЁСw jЙzyka Python
Group:		Applications
Requires:	%{name}-modules = %{version}

%description pydoc
Python interactive module documentation access support.

%description pydoc -l pl
Interaktywne korzystanie z dokumentacji moduЁСw jЙzyka Python.

%package idle
Summary:	IDE for Python language
Summary(pl):	IDE dla jЙzyka Python
Group:		Applications
Requires:	%{name}-modules = %{version}

%description idle
IDE for Python language.

%description idle -l pl
IDE dla jЙzyka Python.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(es):	Bibliotecas y archivos de inclusiСn para construir programas en python
Summary(fr):	BibliothХques et en-tЙtes pour construire du code python
Summary(pl):	Pliki nagЁСwkowe i biblioteki Pythona
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para o Python
Summary(ru):	Библиотеки и хедеры для построения кода на языке Python
Summary(tr):	Python ile geliЧtirme yapmak iГin gerekli dosyalar
Summary(uk):	Б╕бл╕отеки та хедери для програмування на мов╕ Python
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This packages
contains the header files and libraries which are needed to do both of
these tasks.

%description devel -l de
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und lДъt sich in andere Programme
integrieren. Dieses Paket enthДlt die Header-Dateien und Libraries,
die fЭr beide Aufgaben erforderlich sind.

%description devel -l es
El interpretador Python permite incluir con facilidad extensiones
cargadas dinАmicamente. Python es tambiИn fАcil de ser empotrado en
otros programas. Este paquete contiene los archivos de inclusiСn y
bibliotecas necesarios para estas dos tareas.

%description devel -l fr
L'interprИteur Python est relativement facile Ю Иtendre avec des
extensions chargИes dynamiquement et Ю insИrer dans d'autres
programmes. Ce paquetage contient les en-tЙtes et les bibliothХques
nИcessaires Ю ces deux tБches.

%description devel -l pl
Wszystko co potrzebne, aby napisaФ w C/C++ moduЁ rozszerzaj╠cy
mo©liwo╤ci Pythona. S╠ tu rСwnie© wersje ╪rСdЁowe moduЁСw ze
standardowej biblioteki.

%description devel -l pt_BR
O interpretador Python permite incluir com facilidade extensУes
carregadas dinamicamente. Python И tambИm fАcil de ser embutido em
outros programas. Este pacote contИm os arquivos de inclusЦo e
bibliotecas necessАrios para estas duas tarefas.

%description devel -l ru
Интерпретатор Python относительно легко расширяется при помощи
динамически загружаемых расширений и встраивается в другие программы.
Этот пакет содержит хедеры и библиотеки, необходимые для обеих этих
задач.

%description devel -l tr
Bu paket, Python ile geliЧtirme yapЩlabilmesi iГin gerekli baЧlЩk
dosyalarЩnЩ ve kitaplЩklarЩ iГerir.

%description devel -l uk
╤нтерпретатор Python в╕дносно легко розширю╓ться за допомогою
розширень з динам╕чною загрузкою та вбудову╓ться в ╕нш╕ програми. Цей
пакет м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для обох цих задач.

%package devel-src
Summary:	Python module sources
Summary(pl):	Pliki ╪rСdЁowe moduЁСw Pythona
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{version}

%description devel-src
Python module sources.

%description devel-src -l pl
Pliki ╪rСdЁowe moduЁСw Pythona.

%package static
Summary:	Static python library
Summary(pl):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Provides:	%{name}-static = %{py_ver}
Requires:	%{name}-devel = %{version}

%description static
Static python library.

%description static -l pl
Statyczna biblioteka Pythona.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python
Summary(es):	DocumentaciСn para Python
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Pythona
Summary(pt_BR):	DocumentaГЦo para a linguagem de programaГЦo Python
Summary(ru):	Документация по языку Python
Summary(tr):	Python belgeleri
Summary(uk):	Документац╕я по мов╕ Python
Group:		Documentation
Requires:	%{name} = %{version}
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description doc -l de
Dieses Paket enthДlt Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description doc -l es
DocumentaciСn para Python. Contiene archivos en texto y PostScript.

%description doc -l fr
Ce paquetage contient la documentation sur le langage python et sur
son interprИteur sous forme de fichiers ASCII et LaTeX.

%description doc -l pl
Oficjalna dokumentacja do Pythona. Zawiera przykЁadowe programy,
narzЙdzia i dokumentacjЙ. Strony podrЙcznika man znajduj╠ siЙ w
gЁСwnym pakiecie. Ten pakiet nie zawiera ╪rСdeЁ dokumentacji
napisanych w LaTeX'u, tylko gotowe do wykorzystania pliki
postscript'owe i HTML.

%description doc -l pt_BR
O pacote python-doc contИm documentaГЦo para a linguagem de
programaГЦo e para o interpretador Python. Fornecida em arquivos texto
e Postcript.

%description doc -l ru
Этот пакет содержит документацию по собственно языку Python и по
исполняющему его интерпретатору в виде набора текстовых файлов и
исходных текстов в формате LaTeX.

%description doc -l tr
Bu paket, Python dili ile ilgili belgeleri ve dЭz ASCII dosyalarЩ ve
LaTeX kaynaklarЩnЩn bir karЩЧЩmЩ olan yorumlayЩcЩyЩ iГerir.

%description doc -l uk
Цей пакет м╕стить документац╕ю по власне мов╕ Python та по виконуючому
╖╖ ╕нтерпретатору у вигляд╕ набора текстових файл╕в та вих╕дних
текст╕в у формат╕ LaTeX.

%package without-thread
Summary:	Python without threads
Summary(pl):	Pyton bez w╠tkСw
Summary(ru):	Визуальный интерфейс (GUI) для Python
Summary(uk):	В╕зуальний ╕нтерфейс (GUI) для Python
Group:		Libraries/Python
Provides:	%{name}-without-thread = %{py_ver}
Requires:	%{name} = %{version}
Obsoletes:	python-without-thread

%description without-thread
This package is rather needed for apache-mod_python module. Other ways
of use are unknown.

%description without-thread -l pl
Pyton bez w╠tkСw jest wЁa╤ciwie potrzebny tylko moduЁowi
apache-mod_python, bo apache nie ich na razie nie wspiera.

%package -n tkinter
Summary:	Standard Python interface to the Tk GUI toolkit
Summary(de):	Grafischer OberflДche fЭr Python
Summary(es):	Interface GUI para Phyton
Summary(fr):	Interface graphique pour python
Summary(pl):	Standardowy interfejs Pythona do biblioteki Tk
Summary(pt_BR):	Interface GUI para Phyton
Summary(tr):	Python iГin grafik kullanЩcЩ arayЭzЭ
Group:		Libraries/Python
Requires:	%{name}-modules = %{version}
Requires:	tcl >= 8.0.3
Requires:	tk  >= 8.0.3
Requires:	tix >= 4.1.0.6

%description -n tkinter
Standard Python interface to the Tk GUI toolkit.

%description -n tkinter -l de
Eine grafische Schnittstelle fЭr Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description -n tkinter -l es
Una interface grАfica para Python, basada en Tcl/Tk, y usada por
muchas herramientas de configuraciСn.

%description -n tkinter -l fr
Interface graphique pour Python, basИe sur Tcl/Tk et utilisИe par
beaucoup des outils de configuration.

%description -n tkinter -l pl
Standardowy interfejs Pythona do biblioteki Tk.

%description -n tkinter -l pt_BR
Uma interface grАfica para Python, baseada em Tcl/Tk, e usada por
muitas ferramentas de configuraГЦo.

%description -n tkinter -l ru
Графический интерфейс (GUI) для Python, построенный на Tcl/Tk.

%description -n tkinter -l tr
Python iГin Tcl/Tk'ye dayalЩ ve pek Гok ayarlama aracЩ tarafЩndan
kullanЩlan grafik bir arayЭzdЭr.

%description -n tkinter -l uk
Граф╕чний ╕нтерфейс (GUI) для Python, побудований на Tcl/Tk.

%package old
Summary:	Depreciated Python modules
Summary(pl):	Nieaktualne moduЁy jЙzyka Python
Group:		Libraries/Python
Requires:	%{name}-modules = %{version}

%description old
Install this package when one of your program written in Python is old
as Miss Universum of 1918, who only you want to see... ooops, which
only you want to run.

%description old -l pl
Zainstaluj ten pakiet, wtedy kiedy jeden z Twoich programСw napisanych
w jЙzyku Python jest tak stary jak Miss Universum z roku 1918, ktСr╠
tylko ty chcesz zobaczyФ... przepraszam, ktСry tylko ty chcesz
uruchomiФ.

%package examples
Summary:	Example programs in Python
Summary(pl):	PrzykЁadowe programy w Pythonie
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{version}
Obsoletes:	python-tools

%description examples
Example programs in Python.

%description examples -l pl
PrzykЁadowe programy w Pythonie.

%prep
%setup -q -n Python-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

install -d html-doc
tar -xf %{SOURCE1} --use=bzip2 -C html-doc

%build
%{__autoconf}

POSIXLY_CORRECT=TRUE; export POSIXLY_CORRECT

CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure \
	--with-threads \
	--enable-shared

%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

install libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython.so

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}

install -d $RPM_BUILD_ROOT%{_examplesdir}/python
cp -ar Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/python

echo "%defattr(644,root,root,755)" > modules.filelist

find $RPM_BUILD_ROOT%{py_libdir} \
	-type f \
	-maxdepth 1 \
	-printf %{py_libdir}/%f\\n \
	| grep '\.py[co]$' \
	| grep -v -e 'UserDict\.py[oc]$'\
	| grep -v -e 'codecs\.py[oc]$' \
	| grep -v -e 'copy_reg\.py[oc]$' \
	| grep -v -e 'locale\.py[oc]$' \
	| grep -v -e 'posixpath\.py[oc]$' \
	| grep -v -e 'pydoc\.py[oc]$' \
	| grep -v -e 'site\.py[oc]$' \
	| grep -v -e 'stat\.py[oc]$' \
	| grep -v -e 'os\.py[oc]$' \
	| grep -v -e 'encodings\/.*\.py[oc]$' >> modules.filelist

find $RPM_BUILD_ROOT%{py_dyndir} \
	-type f \
	-maxdepth 1 \
	-printf "%%%%attr(755,root,root) %{py_dyndir}/%f\\n" \
	| grep '\.so$' \
	| grep -v -e '_iconv_codec\.so$' \
	| grep -v -e 'readline\.so$' \
	| grep -v -e 'struct\.so$' \
	| grep -v -e '_tkinter\.so$' >> modules.filelist

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%{_mandir}/man1/*

# readline support for python binary
%attr(755,root,root) %{py_dyndir}/readline.so

%files modules -f modules.filelist
%defattr(644,root,root,755)

%dir %{py_libdir}/plat-*
%attr(755,root,root) %{py_libdir}/plat-*/regen
%{py_libdir}/plat-*/*.py[co]

%dir %{py_libdir}/bsddb
%{py_libdir}/bsddb/*.py[co]

%dir %{py_libdir}/compiler
%{py_libdir}/compiler/*.py[co]

%dir %{py_libdir}/curses
%{py_libdir}/curses/*.py[co]

%dir %{py_libdir}/distutils
%{py_libdir}/distutils/*.py[co]

%dir %{py_libdir}/distutils/command
%{py_libdir}/distutils/command/*.py[co]

%dir %{py_libdir}/email
%{py_libdir}/email/*.py[co]

%dir %{py_libdir}/hotshot
%{py_libdir}/hotshot/*.py[co]

%dir %{py_libdir}/logging
%{py_libdir}/logging/*.py[co]

%dir %{py_libdir}/xml
%{py_libdir}/xml/*.py[co]

%dir %{py_libdir}/xml/parsers
%{py_libdir}/xml/parsers/*.py[co]

%dir %{py_libdir}/xml/sax
%{py_libdir}/xml/sax/*.py[co]

%dir %{py_libdir}/xml/dom
%{py_libdir}/xml/dom/*.py[co]

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython*so.*

%dir %{py_dyndir}
%dir %{py_libdir}
%dir %{py_sitedir}

# required shared modules by python library
#%attr(755,root,root) %{py_dyndir}/_iconv_codec.so
%attr(755,root,root) %{py_dyndir}/struct.so

# required modules by python library
%{py_libdir}/UserDict.py[co]
%{py_libdir}/codecs.py[co]
%{py_libdir}/copy_reg.py[co]
%{py_libdir}/locale.py[co]
%{py_libdir}/posixpath.py[co]
%{py_libdir}/site.py[co]
%{py_libdir}/stat.py[co]
%{py_libdir}/os.py[co]

# required encodings by python library
%dir %{py_libdir}/encodings
%{py_libdir}/encodings/*.py[co]

%files pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_libdir}/pydoc.py[co]

%files idle
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/idle
%dir %{py_libdir}/idlelib
%dir %{py_libdir}/idlelib/Icons
%{py_libdir}/idlelib/*.py[co]
%{py_libdir}/idlelib/Icons/*

%files devel
%defattr(644,root,root,755)
%doc Misc/{ACKS,NEWS,README}
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{py_incdir}
%{py_incdir}/*.h

%dir %{py_libdir}/config
%attr(755,root,root) %{py_libdir}/config/makesetup
%attr(755,root,root) %{py_libdir}/config/install-sh
%{py_libdir}/config/Makefile
%{py_libdir}/config/Makefile.pre.in
%{py_libdir}/config/Setup
%{py_libdir}/config/Setup.config
%{py_libdir}/config/Setup.local
%{py_libdir}/config/config.c
%{py_libdir}/config/config.c.in
%{py_libdir}/config/python.o

%files devel-src
%defattr(644,root,root,755)
%attr(-,root,root) %{py_libdir}/*.py
%{py_libdir}/plat-*/*.py
%{py_libdir}/bsddb/*.py
%{py_libdir}/compiler/*.py
%{py_libdir}/curses/*.py
%{py_libdir}/distutils/*.py
%{py_libdir}/distutils/command/*.py
%{py_libdir}/email/*.py
%{py_libdir}/hotshot/*.py
%{py_libdir}/logging/*.py
%{py_libdir}/xml/*.py
%{py_libdir}/xml/parsers/*.py
%{py_libdir}/xml/sax/*.py
%{py_libdir}/xml/dom/*.py
%{py_libdir}/encodings/*.py
%{py_libdir}/idlelib/*.py

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python/Tools
%{_examplesdir}/python/Demo

%files doc
%defattr(644,root,root,755)
%doc html-doc/*
%dir %{py_libdir}/test
%attr(-,root,root) %{py_libdir}/test/*

%files -n tkinter
%defattr(644,root,root,755)

%{py_libdir}/lib-tk
%attr(755,root,root) %{py_dyndir}/_tkinter.so

%files old
%defattr(644,root,root,755)

%dir %{py_libdir}/lib-old
%{py_libdir}/lib-old/*.py[co]
