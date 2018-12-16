message( "\nCommon CMake for KhaOS Studio build system" )

if ( DEFINED ENV{KHAOS_BUILD} )
    set ( CMAKE_LIBRARY_OUTPUT_DIRECTORY "$ENV{KHAOS_BUILD}/lib/${CMAKE_BUILD_TYPE}" )
    set ( CMAKE_ARCHIVE_OUTPUT_DIRECTORY "$ENV{KHAOS_BUILD}/lib/${CMAKE_BUILD_TYPE}" )
    set ( CMAKE_RUNTIME_OUTPUT_DIRECTORY "$ENV{KHAOS_BUILD}/bin/${CMAKE_BUILD_TYPE}" )

    include_directories(BEFORE SYSTEM "$ENV{KHAOS_BUILD}/include/${CMAKE_BUILD_TYPE}")
    link_directories(BEFORE SYSTEM "$ENV{KHAOS_BUILD}/lib/${CMAKE_BUILD_TYPE}")
else()
	message( FATAL_ERROR "The environment variable KHAOS_BUILD is not defined!")
endif()


#if ( DEFINED PUBLISHED_FILES )
#	if ( DEFINED PUBLISHED_TARGET )
#		message( "Files to be published added!\n" )
#
#		# Post-Build Step: Copy library DLL to runtime directory
#		add_custom_command(TARGET ${PUBLISHED_TARGET} POST_BUILD
#			COMMAND ${CMAKE_COMMAND} -E copy_directory
#			"${CMAKE_CURRENT_SOURCE_DIR}/${PUBLISHED_FILES}" "$ENV{KHAOS_BUILD}/include"
#			COMMENT "Copying file to Runtime directory: $ENV{KHAOS_BUILD}/include"
#		)
#	else()
#		message( WARNING "Some files are marked to be published, but not variable PUBLISHED_TARGET was defined..." )
#	endif()
#endif()