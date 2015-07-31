function(loop_list list dest)
    if(ENABLE_CMAKE_DEBUG_OUTPUT)
#        message("dest: ${dest}: ${${dest}}")
#        message("${${list}}")
    endif()
    foreach(var IN LISTS ${list})
        if(ENABLE_CMAKE_DEBUG_OUTPUT)
            message(STATUS "var: ${var}: ${${var}}")
        endif()

        set(var ${${var}})
        list(APPEND ${dest}    ${var}  )
    endforeach()
    
    set(${dest} ${${dest}} PARENT_SCOPE)
endfunction()
# --------------------------------------------------------------------
function(update_libs_includes libs incs)
#    foreach(var ${libs})
#        message(STATUS "var: ${var}: ${${var}}")
#        set(libs ${${libs}})
#        list(APPEND GORGON_LIBRARIES    ${libs}  )
#    endforeach(var list)
    loop_list(libs GORGON_LIBRARIES)
#    loop_list(${libs})
#    message(STATUS "incs: ${incs}: ${${incs}}")
#    set(incs ${${incs}})
#    list(APPEND GORGON_INCLUDE_DIRS ${incs})
    loop_list(incs GORGON_INCLUDE_DIRS)
 
    set(GORGON_LIBRARIES ${GORGON_LIBRARIES} PARENT_SCOPE)
    set(GORGON_INCLUDE_DIRS ${GORGON_INCLUDE_DIRS} PARENT_SCOPE)
    
endfunction()
