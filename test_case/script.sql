USE [NbFileManagement]
GO
/****** Object:  Table [dbo].[Nb_AudioFile]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_AudioFile]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_AudioFile](
	[Id] [uniqueidentifier] NULL,
	[Duration] [float] NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_DocumentFile]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_DocumentFile]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_DocumentFile](
	[Id] [uniqueidentifier] NULL,
	[PageCount] [int] NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_File]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_File]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_File](
	[Id] [uniqueidentifier] NOT NULL,
	[OriginalName] [nvarchar](255) NULL,
	[Name] [nvarchar](255) NULL,
	[Host] [nvarchar](255) NULL,
	[Path] [nvarchar](max) NULL,
	[Type] [nvarchar](255) NULL,
	[Extension] [nvarchar](max) NULL,
	[Size] [bigint] NULL,
	[CreateTime] [datetime] NULL,
	[Md5] [nvarchar](255) NULL,
	[RawInfo] [nvarchar](max) NULL,
	[Format] [nvarchar](255) NULL,
	[SourceType] [nvarchar](255) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_FileBaseRelation]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_FileBaseRelation]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_FileBaseRelation](
	[OriginalFileId] [uniqueidentifier] NULL,
	[DerivedFileId] [uniqueidentifier] NULL,
	[DerivedType] [nvarchar](255) NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_FileProcessState]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_FileProcessState]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_FileProcessState](
	[FileId] [uniqueidentifier] NOT NULL,
	[CurrentState] [nvarchar](255) NULL,
	[IsFinished] [bit] NULL,
	[CreateTime] [datetime] NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_FileReference]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_FileReference]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_FileReference](
	[MD5] [nvarchar](255) NULL,
	[Count] [int] NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_ImageExtension]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_ImageExtension]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_ImageExtension](
	[OriginalFileId] [uniqueidentifier] NULL,
	[FileId] [uniqueidentifier] NULL,
	[ResizeMode] [nvarchar](50) NULL,
	[Width] [int] NULL,
	[Height] [int] NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_ImageFile]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_ImageFile]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_ImageFile](
	[Id] [uniqueidentifier] NULL,
	[Width] [int] NULL,
	[Height] [int] NULL
) ON [PRIMARY]
END
GO
/****** Object:  Table [dbo].[Nb_VideoFile]    Script Date: 2018/3/30 14:25:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Nb_VideoFile]') AND type in (N'U'))
BEGIN
CREATE TABLE [dbo].[Nb_VideoFile](
	[Id] [uniqueidentifier] NULL,
	[Duration] [float] NULL,
	[VideoBitRate] [float] NULL,
	[AudioBitRate] [float] NULL,
	[Width] [int] NULL,
	[Height] [int] NULL,
	[FrameRate] [float] NULL,
	[TotalFrames] [bigint] NULL,
	[AudioChannel] [nvarchar](255) NULL
) ON [PRIMARY]
END
GO
