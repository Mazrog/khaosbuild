message( "\nCommon CMake for KhaOS Studio build system" )

if ( DEFINED ENV{KHAOS_BUILD} )
    set ( CMAKE_LIBRARY_OUTPUT_DIRECTORY "$ENV{KHAOS_BUILD}/lib/${CMAKE_BUILD_TYPE}" )
    set ( CMAKE_ARCHIVE_OUTPUT_DIRECTORY "$ENV{KHAOS_BUILD}/lib/${CMAKE_BUILD_TYPE}" )
    set ( CMAKE_RUNTIME_OUTPUT_DIRECTORY "$ENV{KHAOS_BUILD}/bin/${CMAKE_BUILD_TYPE}" )

    include_directories(BEFORE SYSTEM "$ENV{KHAOS_BUILD}/include/${CMAKE_BUILD_TYPE}")
    link_directories(BEFORE SYSTEM "$ENV{KHAOS_BUILD}/lib/${CMAKE_BUILD_TYPE}")

    macro(publish_files target_name)
        if ( DEFINED LIBRARY_PATH )
            # Post-Build Step: Copy library DLL to runtime directory
            file( COPY "${CMAKE_CURRENT_SOURCE_DIR}/${target_name}/${LIBRARY_PATH}"
                DESTINATION "$ENV{KHAOS_BUILD}/include/${CMAKE_BUILD_TYPE}/"
            )
            message ( "Copying file to Runtime directory: $ENV{KHAOS_BUILD}/include/${CMAKE_BUILD_TYPE}/" )
            unset( LIBRARY_PATH )
        endif()
    endmacro(publish_files)
else()
	message( FATAL_ERROR "The environment variable KHAOS_BUILD is not defined!")
endif()
