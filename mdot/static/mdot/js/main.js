// document.ready shorthand
$(function() {
        
    // async load css by flipping the media attribute to all
    $('link[rel="stylesheet"]').attr('media', 'all');
    
    // truncate feature descriptions
    $('.mdot-resource-desc').succinct({
        size: 65
    });
    
});