var gulp = require('gulp');
var less = require('gulp-less');
var livereload = require('gulp-livereload');

gulp.task('less', function () {
  gulp.src('less/styles.less')
    .pipe(less())
    .pipe(gulp.dest('./dist'))
    .pipe(livereload());
});

gulp.task('watch', function () {
  livereload.listen({quite: true});
  gulp.watch(['./less/**'], ['less']);
  gulp.watch(['./copy/**'], ['copy']);
});

gulp.task('copy', function () {
  gulp.src([
    'node_modules/bootstrap/fonts/*'
  ]).pipe(gulp.dest(
    './dist/fonts'
  ));
});

gulp.task('build', ['copy', 'less']);
gulp.task('default', ['build', 'watch']);