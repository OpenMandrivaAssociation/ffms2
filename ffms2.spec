%define		major 5
%define		libname %mklibname %{name}_ %{major}
%define		devname %mklibname %{name} -d

Summary:		Wrapper library around libffmpeg
Name:		ffms2
Version:		5.0
Release:		1
License:		MIT
Group:		Video
Url:		https://github.com/FFMS/ffms2/
Source0:	https://github.com/FFMS/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		ffms2-5.0-dont-force-seek-when-cannot-be-done.patch
Patch1:		ffms2-5.0-require-ffmpeg-71.patch
BuildRequires:		libtool
BuildRequires:		pkgconfig(libavcodec)
BuildRequires:		pkgconfig(libavformat)
BuildRequires:		pkgconfig(libavutil)
BuildRequires:		pkgconfig(libswresample)
BuildRequires:		pkgconfig(libswscale)
BuildRequires:		pkgconfig(zlib)

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%files
%doc COPYING
%{_bindir}/ffmsindex

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.
This package contains the library itself.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files for development with %{name}.

%files -n %{devname}
%{_includedir}/ffms*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_docdir}/lib%{name}-devel

#---------------------------------------------------------------------------

%prep
%autosetup -p1

sed -i 's/\r$//' COPYING


%build
./autogen.sh
%configure \
	--docdir=%{_docdir}/lib%{name}-devel \
	--enable-shared \
	--disable-static
%make_build


%install
%make_install
