%define name t-crisis
%define version 3.5.12a
%define release 3
%define debug_package %{nil}

Summary:	T-Crisis 3 100% A.I. is a Tetris clone with special modes
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Games/Arcade
License:	Open-Source Freeware unknown
Url:		http://16bitsoft.com/games-TetriCrisis3CPU.htm
Source:		http://16bitsoft.com/files/TC3100CPU/SOURCE/%{name}-%{version}.zip
Source10:	%{name}-128.png
Source11:	%{name}-64.png
Source12:	%{name}-48.png
Source13:	%{name}-32.png
Source14:	%{name}-16.png
Patch1:		t-crisis-3.5.12a-datapath.patch
Patch2:		t-crisis-3.5.12a-makefile.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
Obsoletes:	tetricrisis3 <= %{version}

%description
T-Crisis 3 100% A.I. is a Tetris clone.
- 100% FREE
- Beautiful full color and high resolution visual graphics
- Awesome digital sound effects
- Amazing digitally orchestrated music soundtrack
- 100% arcade perfect GameBoy to PC conversion of the original
- 1 to 3 player simultaneous play
- Fight against two of your friends or the computer players
- Play with keyboard and/or 1 to 2 USB joysticks
- USB joysticks and keyboard can be remapped
- 6 different and exciting game modes (original and the new Crisis+Mode)

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -DPKGDATADIR=\\\"%{_gamesdatadir}/%{name}/data\\\""

%make
%__mv tc3ai %{name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}%{_gamesbindir}
%__install -d %{buildroot}%{_gamesdatadir}/%{name}
cp -R data %{buildroot}%{_gamesdatadir}/%{name}/
%__install -D -m 755 %{name} %{buildroot}%{_gamesbindir}/%{name}

%__install -D -m 644 %{SOURCE14} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D -m 644 %{SOURCE13} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D -m 644 %{SOURCE12} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D -m 644 %{SOURCE11} %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D -m 644 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

%__install -D -m 644 %{SOURCE11} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__install -d %{buildroot}%{_datadir}/applications

%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=T-Crisis 3 100% A.I.
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%files
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/data/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

