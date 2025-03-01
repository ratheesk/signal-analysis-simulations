if (!window.dash_clientside) {
  window.dash_clientside = {};
}

window.dash_clientside.clientside = {
  // Function to toggle the sidebar
  toggleSidebar: function (n_clicks, data) {
    if (!data) {
      data = { collapsed: false };
    }

    const sidebar = document.getElementById('sidebar');

    if (n_clicks) {
      data.collapsed = !data.collapsed;

      if (data.collapsed) {
        sidebar.style.left = '-250px';
      } else {
        sidebar.style.left = '0px';
      }
    }

    // Handle initial state for responsive layouts
    const mediaQuery = window.matchMedia('(max-width: 768px)');
    if (mediaQuery.matches && !n_clicks) {
      sidebar.style.left = '-250px';
      data.collapsed = true;
    }

    return data;
  },

  // Function to update content margin based on sidebar state
  updateContentMargin: function (data) {
    if (!data) {
      data = { collapsed: false };
    }

    const style = {
      transition: 'margin-left 0.3s ease-in-out',
      padding: '2rem',
    };

    if (data.collapsed) {
      style.marginLeft = '0px';
    } else {
      style.marginLeft = '250px';
    }

    // Handle responsive layout
    const mediaQuery = window.matchMedia('(max-width: 768px)');
    if (mediaQuery.matches) {
      style.marginLeft = '0px';
    }

    return style;
  },
};

// Add event listeners for collapsible menu items
document.addEventListener('DOMContentLoaded', function () {
  // This handles toggling the chevron icon for dropdowns
  const toggleButtons = document.querySelectorAll('.sidebar-btn');
  toggleButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const chevron = this.querySelector('.fa-chevron-down');
      chevron.classList.toggle('rotate');
    });
  });

  // Media query for responsive behavior
  const mediaQuery = window.matchMedia('(max-width: 768px)');
  function handleScreenChange(e) {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('page-content');

    if (e.matches) {
      sidebar.style.left = '-250px';
      content.style.marginLeft = '0px';
    } else {
      sidebar.style.left = '0px';
      content.style.marginLeft = '250px';
    }
  }

  mediaQuery.addListener(handleScreenChange);
  // Initial call on page load
  handleScreenChange(mediaQuery);
});
